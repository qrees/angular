'use strict';


// Declare app level module which depends on filters, and services
angular.module('GalleryApp', ['GalleryApp.filters', 'GalleryApp.services', 'GalleryApp.directives', 'GalleryApp.controllers']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/albums', {templateUrl: '/static/partials/album-list.html', controller: 'AlbumListCtrl'});
        $routeProvider.otherwise({redirectTo: '/albums'});
    }]);
