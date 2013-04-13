function AlbumListCtrl($scope, $http) {
    $http.get('/gallery/.json').success(function(data) {
        $scope.list = data;
    });

    $scope.orderProp = 'age';
}

AlbumListCtrl.$inject = ['$scope', '$http'];