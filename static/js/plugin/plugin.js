$(function ($) {
  "use strict";

  jQuery(document).ready(function () {
    /* niceSelect */
    $("select").niceSelect();

    // counter Up
    if (document.querySelector('.counter') !== null) {
      $('.counter').counterUp({
        delay: 10,
        time: 2000
      });
    }

    // card-carousel
    $(".testimonials-carousel").not('.slick-initialized').slick({
      infinite: true,
      autoplay: false,
      focusOnSelect: false,
      speed: 1000,
      slidesToShow: 2,
      slidesToScroll: 1,
      arrows: false,
      prevArrow: "<button type='button' class='slick-prev pull-left'><i class=\"icon-a-left-arrow\"  aria-hidden='true'></i></button>",
      nextArrow: "<button type='button' class='slick-next pull-right'><i class=\"icon-b-right-arrow\"  aria-hidden='true'></i></button>",
      dots: false,
      dotsClass: 'section-dots',
      customPaging: function (slider, i) {
        var slideNumber = (i + 1),
          totalSlides = slider.slideCount;
        return '<a class="dot" role="button" title="' + slideNumber + ' of ' + totalSlides + '"><span class="string">' + slideNumber + '/' + totalSlides + '</span></a>';
      },
      responsive: [
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
          }
        }
      ]
    });

    /* Magnific Popup */
    if (document.querySelector('.popupvideo') !== null) {
      $('.popupvideo').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false,
      });
    }

    /* Countdown js */
    if (document.querySelector('.countdown') !== null) {
      $('.countdown').downCount({
        date: '12/31/2022 11:59:59',
        offset: +10
      });
    }

    /* Datepicker js */
    $("#dateStart").datepicker();
    $("#dateEnd").datepicker();


    /* Apexcharts js */
    if (document.querySelector('.chart') !== null) {
      var options = {
        chart: {
          height: 380,
          type: "line",
          foreColor: '#C4C4C4',
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: "Series",
            data: [-10, 0, -2, 10, 0, -8, 22, 15, 12, 9, 10],
          }
        ],
        colors: ["#109CF1"],
        stroke: {
          curve: 'smooth'
        },
        xaxis: {
          type: 'datetime',
          categories: ['1/11/2021', '2/11/2021', '3/11/2021', '4/11/2021', '5/11/2021', '6/11/2021', '7/11/2021', '8/11/2021', '9/11/2021', '10/11/2021', '11/11/2021'],
          tickAmount: 5,
          labels: {
            formatter: function (value, timestamp, opts) {
              return opts.dateFormatter(new Date(timestamp), 'dd MMM')
            }
          }
        },
        yaxis: {
          min: -20,
          max: 30,
          tickAmount: 5
        },
        responsive: [
          {
            breakpoint: 1000,
            options: {
              chart: {
                height: 200,
              },
            }
          }
        ]
      };
      var profitLossChart = new ApexCharts(document.querySelector(".profitLossChart"), options);
      profitLossChart.render();
      var turnoverChart = new ApexCharts(document.querySelector(".turnoverChart"), options);
      turnoverChart.render();
      var roiChart = new ApexCharts(document.querySelector(".roiChart"), options);
      roiChart.render();
    }

    // Range Slider
    if (document.querySelector('.min-slide') !== null) {
      $(".min-slide").slider({
        orientation: "horizontal",
        range: "min",
        min: 1,
        max: 100,
        value: 50,
        slide: function (event, ui) {
          $(".min-amount").val("" + ui.value);
        }
      });
      $(".min-amount").val("" + $(".min-slide").slider("value"));
    }
    if (document.querySelector('.max-slide') !== null) {
      $(".max-slide").slider({
        orientation: "horizontal",
        range: "min",
        min: 1,
        max: 100,
        value: 50,
        slide: function (event, ui) {
          $(".max-amount").val("" + ui.value);
        }
      });
      $(".max-amount").val("" + $(".max-slide").slider("value"));
    }
    
    /* Wow js */
    new WOW().init();

  });
});



