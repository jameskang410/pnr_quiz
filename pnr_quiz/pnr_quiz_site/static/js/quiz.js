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

app.controller('QuizController', ['$http','$scope',function($http, $scope) {


	//grabbing all questions - needs to be loaded initially and probably on the results/summary page (to be ready for a retry)
	$scope.grabQuestions = function() {
		$http.get("api/quiz/?format=json").success(function(data) {
			$scope.questions_json = data;
		});	
	};

	//runs when page loads
	$scope.init = function () {
		//Updating headers to align with Django CSRF stuff
		$http.defaults.xsrfCookieName = 'csrftoken';
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		//grabbing all of the questions and answers initially
		$scope.grabQuestions();
	};

	$scope.init();


	//Allows users to start the quiz - quiz moves on from intro screen
	$scope.start = function() {
		$scope.id = 0;
		$scope.score = 0;
		$scope.inProgress = true;
		$scope.getQuestion();
	};

	//grabbing a question
	$scope.getQuestion = function() {
		//if all 10 questions have not yet been answered
		if ($scope.id <= 9) {
			$scope.row = $scope.questions_json[$scope.id];

			$scope.question = $scope.row['format_quote'];
			$scope.correct_answer = $scope.row['person'];
		}
		//if all questions have been answered - aka quiz is over
		else {
			$scope.quizOver = true;
		}
	};

    //Check answer
    $scope.submit = function() {
    	if($scope.userAnswer == $scope.correct_answer) {
    		console.log('Hurray');
    		$scope.score++;
    	}
    	else {
    		console.log('Boo');
    		console.log($scope.userAnswer);
    		console.log($scope.correct_answer);
    	}
    };


}]);
