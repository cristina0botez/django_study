jQuery(function($) {
    $('div.inline-group div.tabular').each(function() {
        fs = $(this).find('fieldset');
        h2 = $(this).find('h2:first');
        // Don't collapse if fieldset contains errors
        if (fs.find('div').hasClass('errors'))
            fs.addClass('tabular_collapse');
        else
            fs.addClass('tabular_collapse collapsed');
        // Add toggle link
        h2_text = h2.html() + ' (';
        h2.html(h2_text);
        h2.append('<a class="tabular_collapser collapse-toggle" href="#">' + gettext('Show') + '</a>');
        h2_text = h2.html() + ')';
        h2.html(h2_text);
        h2a = h2.find('a.tabular_collapser');
        h2a.click(function() {
            fs = $(this).parent('h2').parent('fieldset');
            if (!fs.hasClass('collapsed')) {
                fs.addClass('collapsed');
                $(this).html(gettext('Show'));
            } else {
                fs.removeClass('collapsed');
                $(this).html(gettext('Hide'));
            }
        });
    });
});