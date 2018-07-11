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

    function off(){
        $.ajax({
          type: "GET",
          url: '/volume?action=mute',
      })
    }
    $('#off').click(off)

    function up(){
        $.ajax({
          type: "GET",
          url: '/volume?action=up',
      })
    }
    $('#up').click(up)

    function down(){
        $.ajax({
          type: "GET",
          url: '/volume?action=down',
      })
    }
    $('#down').click(down)

    function shuffle(){
        $.ajax({
          type: "GET",
          url: '/play',
      })
    }
    $('#shuffle').click(shuffle)

    function category_shuffle(){
      var category_name = $(this).parent().parent().find('h4').text()
        $.ajax({
          type: "GET",
          url: '/play?sample=' + category_name,
      })
    }
    $('.shuffle').click(category_shuffle)
});
