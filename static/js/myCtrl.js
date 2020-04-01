myApp.controller("myCtrl",function($scope,$http){
	$scope.name="fdf"
	$http({
		method:"GET",
		url:"http://127.0.0.1:8000/api/nutrifile/"
    }).then(function mySuccess(response){
		$scope.myWelcome=response.data;
	},function myError(response){
			$scope.myWelcome='Error';
	});
});