(function(){
'use strict';

/* Controllers */

var controllers = angular.module('GalleryApp.controllers', []);

controllers.controller('AlbumListCtrl', ['$scope', '$http', function($scope, $http) {
    $http.get('/gallery/.json').success(function(data) {
        $scope.list = data;
    });
}]);

})();
