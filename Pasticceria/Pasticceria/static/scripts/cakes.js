function DateDiff(t1, t2) {
    from = moment(t1, 'YYYY-MM-DD');
    to = moment(t2, 'YYYY-MM-DD');
    return to.diff(from, 'days');
}

function displayPopup(myCakes) {

    var str1 = '<div class="row cake-container"><ul class="list-group"><li class="list-group-item cake-list showcase" id="';
    var str2 = '</li></ul></div>';
    var str3 = '<div class="row popup-list"><ul class="list-group"><li class="list-group-item pp">';

    function divGenerator(x) {
        s = '';
        for (var i in x) {
            ing = x[i];
            s = s + i + ' : ' + ing.Quantity + ' ' + ing.Unit + '<br/>';
        }
        return str3 + s + str2;
    }

    for (var c in myCakes) {
        var j = myCakes[c];
        var pr = parseFloat(j.Price);
        var diff = DateDiff(j.Day, day);
        switch (diff) {
            case 0:
                $('#cakesList').append(str1 + c + '"><div class="ava">Abbiamo ' + j.Availability + '</div> ' + c
                    + ' <div class="price">' + pr + ' euro</div>' + divGenerator(j.Ingredients) + str2);
                break;
            case 1:
                pr = (pr * 80) / 100;
                $('#cakesList').append(str1 + c + '"><div class="ava">Abbiamo ' + j.Availability + '</div> ' + c
                    + ' <div class="price">' + pr + ' euro</div>' + divGenerator(j.Ingredients) + str2);
                break;
            case 2:
                pr = (pr * 20) / 100;
                $('#cakesList').append(str1 + c + '"><div class="ava">Abbiamo ' + j.Availability + '</div> ' + c
                    + ' <div class="price">' + pr + ' euro</div>' + divGenerator(j.Ingredients) + str2);
                break;
            default:
        }
    }

    var popup = [];
    $('.popup-list').each(function () {
        popup.push(this);
    });

    document.addEventListener('mousemove',
        function (e) {
            var px = e.pageX;
            var py = e.pageY;
            $('.popup-list').each(function (index, element) {
                $(element).css({ left: (px + 25) + 'px' });
                $(element).css({ top: (py + 25) + 'px' });
            });
        }
    );
}