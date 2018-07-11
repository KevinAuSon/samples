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

    function epi_init() {
      console.log('test')
      var i = 0;

      function epilepsy () {
        var colors = ['red', 'blue', 'pink', 'yellow', 'purple', 'green', 'black', 'cyan', '#808000', 'GreenYellow', 'MediumVioletRed ']
        
        if(i >= 7)
          i = 0;
         i++;

        $('body').css("background-color", colors[i])
      }
      var interval = setInterval(epilepsy, 400);
      setTimeout(function() {
          clearInterval(interval)
      }, 200000);
    }
    
    $('#NyanCat').click(epi_init)
});
