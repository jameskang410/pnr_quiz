var app = angular.module('quizApp', ['angucomplete-alt', 'angular-loading-bar']);

app.config(function($interpolateProvider, $httpProvider) {
    //changing symbols so that it won't interfere with Django
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    
    //updating headers to align with Django CSRF stuff
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

//created a factory that will retrieve an array of people
app.factory('personRetriever', function ($http, $q) {

    var PersonRetriever = new Object();

    PersonRetriever.getpeople = function () {

        //creating a promise object - in this case, using a deferred object using the $q service
        var deferred = $q.defer();

        $http.get("api/persons/?format=json").success(function(data){
            //promise gets resolved with the http get data
            deferred.resolve(data);
        });
        //HTTP get needs to return a promise object. So I guess returning the resolved data
        //as a promise
        return deferred.promise;
    };

    return PersonRetriever;
});

app.factory('questionRetriever', function ($http, $q) {

    var QuestionRetriever = new Object();

    QuestionRetriever.getquestions = function () {

        var deferred = $q.defer();

        $http.get("api/quiz/?format=json").success(function(data){

            deferred.resolve(data);
        });

        return deferred.promise;
    };

    return QuestionRetriever;
});

app.controller('QuizController', ['$http','$scope', '$timeout', 'personRetriever', 'questionRetriever', 'cfpLoadingBar', 
                                function($http, $scope, $timeout, personRetriever, questionRetriever, cfpLoadingBar) {
    //setting up variables for summary page
    $scope.userQuote = "";

    //set focus on input field if it's not hidden
    var setFocus = function(searchField) {
        $timeout(function() {
        // console.log(searchField);
        searchField.focus();
        }, 0);
    };
    
    //Allows users to start the quiz - quiz moves on from intro screen
    $scope.start = function() {
        var gettingPersons = personRetriever.getpeople();
        var gettingQuestions = questionRetriever.getquestions();

        //chaining promises - ensures that data is loaded before doing something else
        //array_people is set, then questions_json is set, then the window loads and question is retrieved
        gettingPersons
        .then(function(data){
            $scope.array_people = data;
            //need to set this early for the dropdown menu later
            $scope.userPerson  = $scope.array_people[0]['person'];
            // console.log($scope.userPerson);
        })
        .then(function(data){
            gettingQuestions
            .then(function(data){
                $scope.questions_json = data;
                // console.log($scope.questions_json);
                $scope.id = 0;
                $scope.score = 0;
                $scope.inProgress = true;
                $scope.quizOver = false;
                $scope.addQuotes = false;
                //arrays to hold user answers
                $scope.user_answer_array = [];
                getQuestion();
            });
        });
    };  

    //grabbing a question
    var getQuestion = function() {
        //if all 10 questions have not yet been answered
        if ($scope.id <= 9) {
            $scope.row = $scope.questions_json[$scope.id];

            $scope.question = $scope.row['format_quote'];
            $scope.correct_answer = $scope.row['person'];
            $scope.answerMode = true;
            setFocus(document.getElementById('search-field_value'));
            // console.log($scope.array_people);
        }
        //if all questions have been answered - aka quiz is over
        else {
            createSummary();
            $scope.quizOver = true;
        }
    };

    //Check answer
    var checkAnswer = function() {
        $scope.user_answer_array.push($scope.userAnswer);

        if($scope.userAnswer == $scope.correct_answer) {
            // console.log('Hurray');
            $scope.score++;
            $scope.correctAnswer = true;
            setFocus(document.getElementById('next-question-button-correct'));
        }

        else {
            // console.log('Boo');
            // console.log($scope.userAnswer);
            // console.log($scope.correct_answer);
            $scope.correctAnswer = false;
            setFocus(document.getElementById('next-question-button-incorrect'));

        }

        $scope.answerMode = false;

    };

    //push to get the next question
    $scope.nextQuestion = function() {
        $scope.id++;
        getQuestion();
        //clearing the input field
        $scope.$broadcast('angucomplete-alt:clearInput');
    }

    //reset - grabbing questions to be ready for restart
    $scope.reset = function() {
        $scope.inProgress = false;
    };

    //called when user selects an answer (basically acts as submit button)
    $scope.answerSelect = function(selected) {

        //selected-object of angulcomplete-alt calls the function with every letter inputted
        if (typeof selected !== "undefined") {
            $scope.userAnswer = selected.originalObject["person"];
            checkAnswer();
        };
    };

    //creating a summary in JSON (ex: questions, answers, user's answers)
    var createSummary = function() {

        $scope.jsonSummary = [];

        for (var i = 0; i < $scope.questions_json.length; i++) {

            $scope.jsonSummary.push({
                question: $scope.questions_json[i]["format_quote"],
                corrAnswer: $scope.questions_json[i]["person"],
                usAnswer: $scope.user_answer_array[i]
            });
        };

        // console.log($scope.questions_json);
        // console.log($scope.user_answer_array);
        // console.log($scope.jsonSummary);
    };

    //allows users to submit quotes
    $scope.userAdd = function(){

        $http.post("api/add/", {"person": $scope.userPerson, "quote": $scope.userQuote}).
            success(function(){
                $scope.addQuotes = true;
                //clearing text
                document.getElementById('user-text-area').value = "";
                $scope.userQuote = "";
                $scope.userPerson  = $scope.array_people[0]['person'];

            }).
            error(function(){
                alert("Server is busy. Please try submitting the quote again!");
            });
    };

    //share on Facebook
    $scope.postFacebook = function() {

        var message = "I got a " + $scope.score + "/10 on the Parks and Rec Quiz!";

        FB.ui(
            {
             method: 'feed',
             name: message,
             link: 'http://www.parksandrecquiz.com',
             picture: 'http://parksandrecquiz.com/static/img/facebook_pic.jpg',
             caption: 'Parks and Rec Quotes Quiz',
             description: 'Test how well YOU know your favorite Parks and Rec characters.',
            }, 
            function(){});
    };

    //testing
    $scope.testing = function(){
        $scope.score = 7;

        $scope.questions_json = [
        {format_quote: "...Time is money, money is power, power is pizza, and pizza is knowledge...",
        person: "April Ludgate",
        quotes_key: 19},
                            ];
        $scope.jsonSummary = [
                                {"question": "...Boring is my middle name...", "corrAnswer": "Leslie Knope", "usAnswer": "Leslie Knope"},
                                {"question": "...All my favorite foods have butter on them; pancakes, toast, popcorn, grapes -- Oh! Butter is my favorite food!...", "corrAnswer": "Leslie Knope" , "usAnswer": "Chris Traeger"},
                                {"question": "...Time is money, money is power, power is pizza, and pizza is knowledge...", "corrAnswer": "April Ludgate" , "usAnswer": "April Ludgate"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Leslie Knope"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Leslie Knope"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Leslie Knope"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Leslie Knope"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Leslie Knope"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Leslie Knope"},
                                {"question": "...What if I get drunk and talk about Darfur too much? Or not enough?...", "corrAnswer": "Leslie Knope" , "usAnswer": "Andy Dwyer"},
                            ];
        $scope.array_people = [
                                {"person":"Andy Dwyer"},
                                {"person":"Ann Perkins"},
                                {"person":"April Ludgate"},
                                {"person":"Ben Wyatt"},
                                {"person":"Chris Traeger"},
                                {"person":"Garth Blundin"},
                                {"person":"Harris Wittels"},
                                {"person":"Jean-Ralphio Saperstein"},
                                {"person":"Jeremy Jamm"},
                                {"person":"Jerry Gergich"},
                                {"person":"Leslie Knope"},
                                {"person":"Mark Brendanawicz"},
                                {"person":"Mona-Lisa Saperstein"},
                                {"person":"Ron Swanson"},
                                {"person":"Tom Haverford"}
                            ];
                $scope.id = 0;
                $scope.score = 8;
                $scope.quizOver = true;
                $scope.inProgress = true;
                //arrays to hold user answers
                $scope.user_answer_array = [];
                getQuestion();

    };

}]);
