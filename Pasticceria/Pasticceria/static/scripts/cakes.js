var str1 = '<div class="row cake-container"><ul class="list-group"><li class="list-group-item cake-list showcase" id="';
var str2 = '</li></ul></div>';
var str3 = '<div class="row popup-list"><ul class="list-group"><li class="list-group-item pp">';

function DateDiff(t1, t2) {
    from = moment(t1, 'YYYY-MM-DD');
    to = moment(t2, 'YYYY-MM-DD');
    return to.diff(from, 'days');
}

function divGenerator(x) {
    s = '';
    for (var i in x) {
        ing = x[i];
        s = s + i + ' : ' + ing.Quantity + ' ' + ing.Unit + '<br/>';
    }
    return str3 + s + str2;
}

function appendPopup(cake, name, price) {
    $('#cakesList').append(str1 + name + '"><div class="ava">Qta. ' + cake.Availability + '</div> ' + name
        + ' <div class="price">' + price + ' euro</div>' + divGenerator(cake.Ingredients) + str2);
}

function displayPopup(myCakes) {

    for (var c in myCakes) {
        var j = myCakes[c];
        var pr = parseFloat(j.Price);
        var diff = DateDiff(j.Day, day);
        switch (diff) {
            case 0:
                appendPopup(j, c, pr.toFixed(2));
                break;
            case 1:
                pr = (pr * 80) / 100;
                appendPopup(j, c, pr.toFixed(2));
                break;
            case 2:
                pr = (pr * 20) / 100;
                appendPopup(j, c, pr.toFixed(2));
                break;
            default:
        }
    }

    document.addEventListener('mousemove',
        function (e) {
            var px = e.clientX;
            var py = e.clientY;
            $('.popup-list').each(function (index, element) {
                $(element).css({ left: (px + 25) + 'px' });
                $(element).css({ top: (py + 25) + 'px' });
            });
        }
    );
}