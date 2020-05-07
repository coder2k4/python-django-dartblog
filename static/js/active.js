$(document).ready(function () {

    // Активация пунктов меню
    // (() => {
    //     const menu = document.querySelectorAll('.menu a');
    //     Object.keys(menu).forEach((key) => {
    //         if (window.location.href === menu[key].href)
    //             console.log(menu[key].parentElement.classList.toggle('active'))
    //     })
    // })()


    var filterFns = {
        numberGreaterThan50: function () {
            var number = $(this).find('.number').text();
            return parseInt(number, 10) > 50;
        },
        ium: function () {
            var name = $(this).find('.name').text();
            return name.match(/ium$/);
        }
    };
    $('.filters-button-group').on('click', 'button', function () {
        var filterValue = $(this).attr('data-filter');
        filterValue = filterFns[filterValue] || filterValue;
        $grid.isotope({
            filter: filterValue
        });
    });
    $('.button-group').each(function (i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });
});