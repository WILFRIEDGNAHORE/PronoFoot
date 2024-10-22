$(function ($) {
  "use strict";

  jQuery(document).ready(function () {

    // preloader
    $("#preloader").delay(300).animate({
      "opacity": "0"
    }, 500, function () {
      $("#preloader").css("display", "none");
    });

    // Scroll Top
    var ScrollTop = $(".scrollToTop");
    $(window).on('scroll', function () {
      if ($(this).scrollTop() < 500) {
        ScrollTop.removeClass("active");
      } else {
        ScrollTop.addClass("active");
      }
    });
    $('.scrollToTop').on('click', function () {
      $('html, body').animate({
        scrollTop: 0
      }, 500);
      return false;
    });

    // Navbar Dropdown
    $(window).resize(function () {
      if ($(window).width() < 992) {
        $(".dropdown-menu").removeClass('show');
      }
      else {
        $(".dropdown-menu").addClass('show');
      }
    });
    if ($(window).width() < 992) {
      $(".dropdown-menu").removeClass('show');
    }
    else {
      $(".dropdown-menu").addClass('show');
    }

    // User Active
    $('.single-item .user-btn').on('click', function () {
      $('.user-content').toggleClass('active');
      $('.settings-content').removeClass('active');
      $('.cart-content').removeClass('active');
      $('.notifications-content').removeClass('active');
    });
    $('.single-item .notifications-btn').on('click', function () {
      $('.notifications-content').toggleClass('active');
      $('.user-content').removeClass('active');
      $('.settings-content').removeClass('active');
      $('.cart-content').removeClass('active');
    });
    $('.single-item .settings-btn').on('click', function () {
      $('.settings-content').toggleClass('active');
      $('.user-content').removeClass('active');
      $('.notifications-content').removeClass('active');
      $('.cart-content').removeClass('active');
    });
    $('.single-item .cart-btn').on('click', function () {
      $('.cart-content').toggleClass('active');
      $('.user-content').removeClass('active');
      $('.settings-content').removeClass('active');
      $('.notifications-content').removeClass('active');
    });

    // Sticky Header
    var fixed_top = $(".header-section");
    $(window).on("scroll", function () {
      if ($(window).scrollTop() > 50) {
        fixed_top.addClass("animated fadeInDown header-fixed");
      }
      else {
        fixed_top.removeClass("animated fadeInDown header-fixed");
      }
    });

    // Modal active
    $(".login").on("click", function () {
        $("#loginArea").addClass("show").addClass("active");
        $("#regArea").removeClass("show").removeClass("active");
        $("#loginArea-tab").addClass("active");
        $("#regArea-tab").removeClass("active");
    });
    $(".reg").on("click", function () {
        $("#regArea").addClass("show").addClass("active");
        $("#loginArea").removeClass("show").removeClass("active");
        $("#loginArea-tab").removeClass("active");
        $("#regArea-tab").addClass("active");
    });

    // social link active
    var socialLink = $(".social-link a");
    $(socialLink).on('mouseover', function () {
      $(socialLink).removeClass('active');
      $(this).addClass('active');
    });

    // grid and list style
    $(".grid-btn").on("click", function () {
      $(".grid-btn").addClass("active");
      $(".list-btn").removeClass("active");

      $(".single-item").removeClass("list");
      $("#grid").addClass("active");
      $("#list").removeClass("active");
    });
    $(".list-btn").on("click", function () {
      $(".list-btn").addClass("active");
      $(".grid-btn").removeClass("active");

      $(".single-item").addClass("list");
      $("#list").addClass("active");
      $("#grid").removeClass("active");
    });

  });
});