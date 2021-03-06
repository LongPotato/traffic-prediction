'use strict';   // See note about 'use strict'; below

var myApp = angular.module('myApp', [
 'ngRoute',
]);

myApp.controller('myController', function($scope, $http) {
  $scope.roadId = "";
  $scope.direction = "";
  $scope.day = "";
  $scope.time = "";
  $scope.traffic = "";
  $scope.predict = "";

  var url = "http://127.0.0.1:5000";

  $scope.trainModel = function() {
    var model = {
      roadId: $scope.roadId,
      direction: $scope.direction,
      day: $scope.day,
      time: $scope.time,
      traffic: $scope.traffic
    }
    console.log(model);
    $http.post(url + "/train", model)
    .success(function (data, status) {
      console.log("Success", data);
    })
    .error(function (data, status) {
      console.log("Error");
    });
  }

  $scope.getPrediction = function() {
    var model = {
      roadId: $scope.roadId,
      direction: $scope.direction,
      day: $scope.day,
      time: $scope.time,
    }
    console.log(model);
    $http.post(url + "/predict", model)
    .success(function (data, status) {
      console.log("Success", data);
      $scope.predict = data;
    })
    .error(function (data, status) {
      console.log("Error");
    });
  }
});
