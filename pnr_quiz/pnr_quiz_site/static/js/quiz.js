var app = angular.module('quizApp', ['angucomplete-alt', 'angular-loading-bar', 'ngAnimate']);

//Changing the template tags so that they don't conflict
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

//Updating $http headers to align with Django CSRF stuff
// function run($http) {
//   $http.defaults.xsrfHeaderName = 'X-CSRFToken';
//   $http.defaults.xsrfCookieName = 'csrftoken';
// };

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


app.controller('QuizController', ['$http','$scope', '$timeout', 'personRetriever', function($http, $scope, $timeout, personRetriever) {

    //retrieving list of people through the PersonRetriever factory
    //first returning a promise object
    $scope.array_people = personRetriever.getpeople();
    //promise object is resolved using then method, results are in data
    //data is initially just a big JSON, but angucomplete has a title-field="person" field which pulls the person data only
    $scope.array_people.then(function(data){
        $scope.array_people = data;
    });

    //grabbing all questions - needs to be loaded initially and probably on the results/summary page (to be ready for a retry)
    var grabQuestions = function() {
        $http.get("api/quiz/?format=json").success(function(data) {
            $scope.questions_json = data;
        }); 
    };

    //set focus on input field if it's not hidden
    setFocus = function(searchField) {
        $timeout(function() {
        // console.log(searchField);
        searchField.focus();
        }, 0);
    };

    //runs when page loads
    $scope.init = function () {
        //updating headers to align with Django CSRF stuff
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        //grabbing all of the questions and answers initially
        grabQuestions();
    };

    $scope.init();
    
    //Allows users to start the quiz - quiz moves on from intro screen
    $scope.start = function() {
        $scope.id = 0;
        $scope.score = 0;
        $scope.inProgress = true;
        $scope.quizOver = false;
        // console.log($scope.id);
        // console.log($scope.score);
        getQuestion();
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
            $scope.quizOver = true;
        }
    };

    //Check answer
    var checkAnswer = function() {
        
        if($scope.userAnswer == $scope.correct_answer) {
            console.log('Hurray');
            $scope.score++;
            $scope.correctAnswer = true;
        }

        else {
            console.log('Boo');
            console.log($scope.userAnswer);
            console.log($scope.correct_answer);
            $scope.correctAnswer = false;
        }

        $scope.answerMode = false;
        setFocus(document.getElementById('next-question-button'));

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
        grabQuestions();

    };

    //called when user selects an answer (basically acts as submit button)
    $scope.answerSelect = function(selected) {

        //selected-object of angulcomplete-alt calls the function with every letter inputted
        if (typeof selected !== "undefined") {
            $scope.userAnswer = selected.title;
            checkAnswer();
        };
    };

    //testing
    // $scope.update = function(){
    //     console.log('TEST');
    //     $scope.array_people = $scope.array_people;
    // };

}]);
