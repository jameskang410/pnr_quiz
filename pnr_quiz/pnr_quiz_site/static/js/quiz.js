var app = angular.module('quizApp', []);

//Changing the template tags so that they don't conflict
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

// // Using the quizApp instance held in the 'app' object
// app.directive('quiz', function() {
// 	return {
// 		restrict: 'AE',
// 		scope: {},
// 		templateUrl: ''
// 	}
// }