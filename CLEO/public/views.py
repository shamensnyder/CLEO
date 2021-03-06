# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from CLEO.extensions import login_manager
from CLEO.public.forms import LoginForm, l2circuitForm
from CLEO.user.forms import RegisterForm
from CLEO.user.models import User
from CLEO.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('public/home.html', form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/automation/')
def automation():
    """Automation page."""
    form = LoginForm(request.form)
    return render_template('public/automation.html', form=form)

@blueprint.route('/as/')
@login_required
def accessSwitch():
    """as page."""
    form = LoginForm(request.form)
    return render_template('public/as.html', form=form)', form=form)
    
@blueprint.route('/mpr/')
@login_required
def mpr():
    """mpr page."""
    form = LoginForm(request.form)
    return render_template('public/mpr.html', form=form)', form=form)

@blueprint.route('/l2circuit/')
@login_required
def l2circuit():
    """l2circuit page."""
    form = l2circuitForm()
    return render_template('public/l2circuit.html', form=form)', form=form)

