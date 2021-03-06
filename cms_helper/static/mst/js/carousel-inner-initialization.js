$(document).ready(function () {
    $(".carusel").owlCarousel({
        items: 1,
        singleItem:true,
        pagination: false,
        mouseDrag: true,
        beforeInit:function(){
          this.$elem.after('<table><tbody><tr><td class="buttom buttonLeft"><img src="/static/mst/img/leftButton.png" alt=""></td><td class="pagenavigation"></td><td class="buttom buttonRight"><img src="/static/mst/img/rightButton.png" alt=""></td></tr></tbody></table>');
        },
        afterInit: function () {
            this.$elem.next().find("td.pagenavigation").html(this.currentItem + 1 + " / " + this.$owlItems.length);
            var that = this.$elem;
            this.$elem.next().find("td.buttonLeft").click({that: that},function (event) {            	
            	event.data.that.trigger('owl.prev');
            });
            this.$elem.next().find("td.buttonRight").click({that: that},function (event) {
            	event.data.that.trigger('owl.next');
            });
        },
        afterMove: function () {
            this.$elem.next().find("td.pagenavigation").html(this.currentItem + 1 + " / " + this.$owlItems.length);
        }
    });
});
