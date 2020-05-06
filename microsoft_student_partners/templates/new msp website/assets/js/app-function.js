'use strict';
/* ==============================================
/*  maps
=============================================== */
//CONTACT US PAGE MAP

function initMap(lat, lng) {
  // The location of office
  var location = {
    lat: parseFloat(lat),
    lng: parseFloat(lng)
  }; // The map, centered at office

  var map_id = document.getElementById("map");
  var map = new google.maps.Map(map_id, {
    zoom: 15,
    center: location,
    styles: [{
      "featureType": "water",
      "elementType": "geometry",
      "stylers": [{
        "color": "#e9e9e9"
      }, {
        "lightness": 17
      }]
    }, {
      "featureType": "landscape",
      "elementType": "geometry",
      "stylers": [{
        "color": "#f5f5f5"
      }, {
        "lightness": 20
      }]
    }, {
      "featureType": "road.highway",
      "elementType": "geometry.fill",
      "stylers": [{
        "color": "#ffffff"
      }, {
        "lightness": 17
      }]
    }, {
      "featureType": "road.highway",
      "elementType": "geometry.stroke",
      "stylers": [{
        "color": "#ffffff"
      }, {
        "lightness": 29
      }, {
        "weight": 0.2
      }]
    }, {
      "featureType": "road.arterial",
      "elementType": "geometry",
      "stylers": [{
        "color": "#ffffff"
      }, {
        "lightness": 18
      }]
    }, {
      "featureType": "road.local",
      "elementType": "geometry",
      "stylers": [{
        "color": "#ffffff"
      }, {
        "lightness": 16
      }]
    }, {
      "featureType": "poi",
      "elementType": "geometry",
      "stylers": [{
        "color": "#f5f5f5"
      }, {
        "lightness": 21
      }]
    }, {
      "featureType": "poi.park",
      "elementType": "geometry",
      "stylers": [{
        "color": "#dedede"
      }, {
        "lightness": 21
      }]
    }, {
      "elementType": "labels.text.stroke",
      "stylers": [{
        "visibility": "on"
      }, {
        "color": "#ffffff"
      }, {
        "lightness": 16
      }]
    }, {
      "elementType": "labels.text.fill",
      "stylers": [{
        "saturation": 36
      }, {
        "color": "#333333"
      }, {
        "lightness": 40
      }]
    }, {
      "elementType": "labels.icon",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "transit",
      "elementType": "geometry",
      "stylers": [{
        "color": "#f2f2f2"
      }, {
        "lightness": 19
      }]
    }, {
      "featureType": "administrative",
      "elementType": "geometry.fill",
      "stylers": [{
        "color": "#fefefe"
      }, {
        "lightness": 20
      }]
    }, {
      "featureType": "administrative",
      "elementType": "geometry.stroke",
      "stylers": [{
        "color": "#fefefe"
      }, {
        "lightness": 17
      }, {
        "weight": 1.2
      }]
    }]
  }); // The marker, positioned at location

  var marker = new google.maps.Marker({
    position: location,
    map: map,
    icon: 'assets/imgs/map-icon.png'
  });
} // initialize all the maps and apis


function initialize() {
  if ($("#map").length > 0) {
    var lat = $("#map").attr('data-lat');
    var lng = $("#map").attr('data-lng');
    initMap(lat, lng);
  }
}
/*===============================================*/

/*  PRE LOADING
 /*===============================================*/


jQuery(window).on('load', function () {
  jQuery('.preloader').delay(500).fadeOut('slow');
  initialize();
});
jQuery(document).ready(function () {
  'use strict';
  /*=============================================== */

  /*   wow
   /* =============================================== */

  var wow = new WOW({
    boxClass: 'wow',
    // animated element css class (default is wow)
    animateClass: 'animated',
    // animation css class (default is animated)
    offset: 0,
    // distance to the element when triggering the animation (default is 0)
    mobile: true,
    // trigger animations on mobile devices (default is true)
    live: true,
    // act on asynchronously loaded content (default is true)
    scrollContainer: null,
    // optional scroll container selector, otherwise use window,
    resetAnimation: true // reset animation on end (default is true)

  });
  wow.init();
  /* ==============================================
   STICKY HEADER
   =============================================== */

  jQuery(window).on('scroll', function () {
    if (jQuery(window).scrollTop() < 100) {
      jQuery('.header').removeClass('sticky_header');
    } else {
      jQuery('.header').addClass('sticky_header');
    }

    if (jQuery(window).scrollTop() < 400) {
      jQuery('.back-to-top').removeClass('active');
    } else {
      jQuery('.back-to-top').addClass('active');
    }
  });
  jQuery('a.has_sub_menu').on('click', function (e) {
    if (window.matchMedia('(max-width: 992px)').matches) {
      e.preventDefault();
      jQuery(this).toggleClass("active_menu");
      jQuery(this).next(jQuery('.sub_menu')).slideToggle();
    }
  });
  /* ==============================================
      Fixed Footer
       =============================================== */

  var exFooter = jQuery('.footer');

  if (exFooter.length) {
    var h = jQuery('.footer').outerHeight();
    jQuery('.page-warp').css('margin-bottom', h);
  }
  /* ==============================================
      Easing move links
       =============================================== */


  jQuery('a.ease[href^="#"]').on('click', function (event) {
    var jQueryanchor = jQuery(this);
    jQuery('html, body').stop().animate({
      scrollTop: jQuery(jQueryanchor.attr('href')).offset().top
    }, 1500, 'easeInOutExpo');
    event.preventDefault();
  });
  /* ==============================================
      Sliders
       =============================================== */

  $('.testimonialslider').owlCarousel({
    loop: true,
    margin: 10,
    items: 1
  });
  $('.teamSlider').owlCarousel({
    loop: true,
    margin: 10,
    items: 3,
    nav: true,
    dots: false,
    navText: ['<i class="fas fa-angle-double-left"></i>', '<i class="fas fa-angle-double-right"></i>'],
    responsive: {
      // breakpoint from 0 up
      0: {
        items: 1
      },
      // breakpoint from 600 up
      700: {
        items: 2
      },
      // breakpoint from 900 up
      992: {
        items: 3
      }
    }
  });
  $('.brand-carousel').owlCarousel({
    loop: true,
    autoplay: true,
    margin: 10,
    items: 6,
    nav: false,
    dots: false,
    responsive: {
      // breakpoint from 0 up
      0: {
        items: 2
      },
      // breakpoint from 600 up
      700: {
        items: 4
      },
      // breakpoint from 900 up
      992: {
        items: 6
      }
    }
  });
  /* --------------------------------------------------------
  COUNTER JS
  ----------------------------------------------------------- */

  jQuery('.counter').counterUp({
    delay: 5,
    time: 3000
  });
  /* ==============================================
      portfolio
      =============================================== */
  // filter items on button click

  jQuery('.portfolio-categories').on('click', 'li', function (e) {
    e.preventDefault();
    jQuery('.portfolio-categories li').removeClass('active');
    jQuery(this).closest('li').addClass('active');
  });
  var filterizd = $('.filtr-container');

  if (filterizd.length > 0) {
    filterizd.filterizr({
      layout: 'sameWidth'
    });
  }
  /* ==============================================
      pop up
      =============================================== */


  jQuery('.filtr-container').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1] // Will preload 0 - before current, and 1 after the current image

    },
    image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
      titleSrc: function titleSrc(item) {
        return item.el.attr('title');
      }
    },
    zoom: {
      enabled: true,
      duration: 300,
      // don't foget to change the duration also in CSS
      opener: function opener(element) {
        return element.find('img');
      }
    }
  });
});