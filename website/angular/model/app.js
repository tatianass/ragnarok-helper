var app = angular.module("app", ["ngRoute", 'ngClickCopy']);

app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "initial.html"
    })
    .when("/about-us", {
        templateUrl : "about-us.html"
    });
});