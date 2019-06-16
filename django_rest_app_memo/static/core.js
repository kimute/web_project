
var djangoMemo = angular.module('djangoMemo', []);

function mainController($scope, $http) {

    $scope.readMemo = function() {
        $http.get('/api/Memo/')
            .success(function(data) {
                $scope.formData = {};
                $scope.Memo = data;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.createMemo = function() {
        $http.post('/api/Memo/', $scope.formData)
            .success(function(data) {
                console.log(data);
                $scope.readMemo();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.deleteMemo = function(id) {
        $http.delete('/api/Memo/' + id + '/')
            .success(function(data) {
                console.log(data);
                $scope.readMemo();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.readMemo();

}
