import csv
from flask import render_template

from . import core
from .forms import FileForm
from .manager import get_routes_results


@core.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@core.route('/', methods=['GET', 'POST'])
def index():

    form = FileForm()
    context = {'form': form}

    if form.validate_on_submit():

        try:
            # build a csv reader out of the StorageFile input
            file_reader = csv.reader(form.data.get('upload'))

            # get the routes results for the reader data
            results = get_routes_results(file_reader)
            # if there's not routes results, add an informative message
            if not results:
                form.errors['upload'] = ['No routes found!']
            else:
                # update context with the results
                context.update({'results': results})
        except Exception as e:
            # in exceptions case, update the form error field
            form.errors['upload'] = [str(e)]

    return render_template('index.html', **context)


@core.route('about', methods=['GET'])
def about():
    return render_template('about.html')
