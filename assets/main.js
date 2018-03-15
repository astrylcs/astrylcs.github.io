/* globals $ */

$(function () {
  $('#pull').on('click', function (e) {
    $('nav ul').slideToggle()
  })
})

$(window).scroll(function () {
  $('#main').css('background-position', '100% ' + parseInt(-$(this).scrollTop() / 3) + 'px' + ', 0%, center top')
})
