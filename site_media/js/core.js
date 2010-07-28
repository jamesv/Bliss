/* Facebook social bits*/

window.fbAsyncInit = function() {
    FB.init({appId: '105150512871756', status: true, cookie: true, xfbml: true});
};

(function() {
    var e = document.createElement('script'); e.async = true;
    e.src = document.location.protocol + '//connect.facebook.net/en_US/all.js';
    document.getElementById('fb-root').appendChild(e);
}());

/* Google Analytics */
var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-639236-21']);
    _gaq.push(['_trackPageview']);

(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();