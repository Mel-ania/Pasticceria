function pop(myCakes) {
    newCakes = myCakes;

    var show = $('.showcase');
    var btnAdd = '<button class="btn btn-add">+</button>';
    var btnSub = '<button class="btn btn-sub">-</button>';

    var pop1 = '<div class="popup" id="popup-'
    var pop2 = '"><div class="content"><div class="close-btn">x</div><div class="btn-container"><h1>';
    var pop3 = '</div></div></div> ';

    show.each(function (index, element) {
        var idName = $(element).attr('id');
        var available = myCakes[idName].Availability;
        $(element).append(pop1 + idName + pop2 + idName + '</h1><p class="text">Cambia la disponibilita.</p>' +
            btnAdd + '<p class="qta"> qta. ' + available + ' </p>' + btnSub + pop3);

        element.addEventListener('click', function (e) {
            $('#popup-' + idName).addClass("active");
        });

        $('.popup').click(function (e) {
            e.stopPropagation();
        }); 

        var docAva = $('#' + idName + ' .ava');
        var qta = $('#popup-' + idName + ' .qta');
        var ba = $('#popup-' + idName + ' .btn.btn-add');
        var bs = $('#popup-' + idName + ' .btn.btn-sub');
        var bc = $('#popup-' + idName + ' .close-btn');

        ba[0].onclick = function (e) {
            var avail = parseInt(newCakes[idName].Availability);
            var ava = avail + 1;
            qta.html(" qta. " + ava + " ");
            newCakes[idName].Availability = ava;
            docAva.html("Qta. " + ava);
        }
        bs[0].onclick = function (e) {
            var avail = parseInt(newCakes[idName].Availability);
            if (avail > 0) {
                var ava = avail - 1;
                qta.html(" qta. " + ava + " ");
                newCakes[idName].Availability = ava;
                docAva.html("Qta. " + ava);
            }
        }
        bc[0].onclick = function (e) {
            $('#popup-' + idName).removeClass("active");
        }
    });
}