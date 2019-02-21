(function () {
    'use strict';

    /**
     * Implementing Ragnarok controller
     * @author Tatiana Saturno
     */
    app.service("RagnarokService", [
        '$http', '$q',
        function ($http, $q) {
            var self = this;
            var deferred = $q.defer();

            $http.get('assets/json/cook_list.json').then(function(data){
                deferred.resolve(data.data);            
            });

            self.getData = function() {
                return deferred.promise;
            };
        }
    ]);
})();
