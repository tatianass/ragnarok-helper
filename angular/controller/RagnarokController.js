(function () {
    'use strict';

    /**
     * Implementing Ragnarok controller
     * @author Tatiana Saturno
     */
    app.controller("RagnarokController", [
        'RagnarokService',
        function (RagnarokService) {
            var self = this;
            var promise = RagnarokService.getData();
            
            promise.then(function (data){
                self.list = data;
            });

            self.search = "recipe_name"
        }
    ]);
})();
