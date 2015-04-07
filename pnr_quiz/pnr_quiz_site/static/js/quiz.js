var app = angular.module('quizApp', []);

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

// Connecting API links to template
app.controller('QuizController', ['$http','$scope',function($http, $scope) {

	$http.defaults.xsrfCookieName = 'csrftoken';
	$http.defaults.xsrfHeaderName = 'X-CSRFToken';


	//Allows users to start the quiz - quiz moves on from intro screen
	$scope.start = function() {
		$scope.id = 0;
		$scope.score = 0;
		$scope.inProgress = true;
		$scope.grabQuestions();
		console.log($scope.randumb);
	};

	//grabbing all questions
	$scope.grabQuestions = function() {
		$http.get("api/quiz/?format=json").success(function(data) {
			$scope.questions_json = data;
			$scope.randumb = 'yahoo';
		});	
	};

	//grabbing a question
	$scope.getQuestion = function() {
		//if all 10 questions have not yet been answered
		if ($scope.id <= 9) {
			$scope.row = [];
			$scope.row = $scope.questions_json[$scope.id];
			console.log($scope.questions_json);
			$scope.question = row['format_quote'];
			$scope.correct_answer = row['person'];
		}
		//if all questions have been answered - aka quiz is over
		else {
			$scope.quizOver = true;
		}
	};


	// $http.get("api/quiz/").success(function(data){
	// 	$scope.
	// });


	// $scope.question = "";
	// $scope.correct_answer = "";

 //    $http.get("api/quiz/").success(function(data){
 //    	$scope.question = data.format_quote;
 //    	$scope.correct_answer = data.person;
 //    });

    //Check answer
    $scope.submit = function() {
    	if($scope.userAnswer == $scope.correct_answer) {
    		console.log('Hurray');
    		$scope.score++;
    		console.log($scope.score);
    	}
    	else {
    		console.log('Boo');
    		console.log($scope.userAnswer);
    		console.log($scope.correct_answer);
    	}
    };


}]);
