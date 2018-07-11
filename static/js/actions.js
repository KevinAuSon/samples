$( document ).ready(function() {
      function play(){
        var url=$(this).attr('id');

        $.ajax({
          type: "GET",
          url: '/play?sample='+url,
      })
    }
    $('.sample-btn').click(play)

    function stop(){
        $.ajax({
          type: "GET",
          url: '/stop',
      })
    }
    $('#stop').click(stop)

    function reboot(){
        $.ajax({
          type: "GET",
          url: '/reboot',
      })
    }
    $('#reboot').click(reboot)
});
