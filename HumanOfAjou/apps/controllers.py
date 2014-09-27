# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, flash, redirect, make_response, jsonify
from apps import app, db
from sqlalchemy import desc
from google.appengine.api import images
from apps.models import Humans, Ajou, ViewRecord, LikeRecord
from apps.forms import HumansForm, AjouForm
from google.appengine.ext import blobstore
from werkzeug.http import parse_options_header
import logging
import json
from apps.APIResponse import APIResponse


@app.route('/', methods=['GET'])
def humans_list():
    context = {}
    humans_list = Humans.query.order_by(desc(Humans.date_created)).all()
    context['humans_list'] = humans_list

    return render_template("index.html", context=context, active_tab='humans_tab', title='HUMANS')


@app.route('/<int:id>', methods=['GET'])
def humans_detail(id):
    humans = Humans.query.get(id)

    try:
        exist_view = ViewRecord.query.filter_by(humans=humans, ip=request.remote_addr).count()
    except:
        exist_view = None

    if exist_view:
        pass
    else:
        vr = ViewRecord(
            humans=humans,
            ip=request.remote_addr
        )
        db.session.add(vr)
        db.session.commit()

        humans.view_count = humans.view_count + 1
        db.session.commit()
    return render_template("humans/detail.html", humans=humans, active_tab='humans_tab', title='HUMANS')


@app.route('/humans/like', methods=['POST'])
def humans_like():
    request_data = json.loads(request.data)
    humans_id = request_data.get('humans_id')

    humans = Humans.query.get(humans_id)

    try:
        exist_like = LikeRecord.query.filter_by(humans=humans, ip=request.remote_addr).count()
    except:
        exist_like = None

    if exist_like:
        return jsonify(
            APIResponse(
                APICode=409,
                APIMessage=u"이미 좋아요 했습니다."
            ).generate
        )
    else:
        like_record = LikeRecord(
            humans=humans,
            ip=request.remote_addr
        )
        db.session.add(like_record)
        db.session.commit()

        humans.like_count = humans.like_count + 1
        db.session.commit()

        return jsonify(
            APIResponse(
                APICode=200,
                APIMessage=u"좋아요 했습니다.",
                APIPayload=humans.like_count
            ).generate
        )


@app.route('/manager', methods=['GET'])
def manager():
    context = {}
    humans_list = Humans.query.order_by(desc(Humans.date_created)).all()
    context['humans_list'] = humans_list

    return render_template("manager/list.html", context=context, active_tab='managerHuman_tab')


@app.route('/manager/humans/create/', methods=['GET', 'POST'])
def manager_humans_create():
    form = HumansForm()
    upload_url = blobstore.create_upload_url('/manager/humans/create/')
    if request.method == 'POST':
        if form.validate_on_submit():
            blob_key = None
            f = request.files['photo']
            if f:
                header = f.headers['Content-Type']
                parsed_header = parse_options_header(header)
                blob_key = parsed_header[1]['blob-key']

            humans = Humans(
                text=form.text.data,
                q_month=form.q_month.data,
                photo=blob_key
            )

            db.session.add(humans)
            db.session.commit()

            flash(u'게시글을 작성하였습니다.', 'success')
            return redirect(url_for('humans_list'))

    return render_template('manager/create.html', form=form, upload_url=upload_url)


@app.route('/manager/humans/update/<int:id>', methods=['GET', 'POST'])
def manager_humans_update(id):
    humans = Humans.query.get(id)

    form = HumansForm(request.form, obj=humans)
    upload_url = blobstore.create_upload_url('/manager/humans/update/' + str(humans.id))
    if request.method == 'POST':
        if form.validate_on_submit():
            previous = humans.photo
            form.populate_obj(humans)
            f = request.files['photo']
            if f:
                header = f.headers['Content-Type']
                parsed_header = parse_options_header(header)
                blob_key = parsed_header[1]['blob-key']
                humans.photo = blob_key
            else:
                humans.photo = previous

            db.session.commit()
        return redirect(url_for('humans_list', id=id))

    return render_template('manager/update.html', form=form, upload_url=upload_url)


@app.route('/manager/humans/delete/<int:id>', methods=['GET'])
def manager_humans_delete(id):
    humans = Humans.query.get(id)

    db.session.delete(humans)
    db.session.commit()

    flash(u'게시글을 삭제하였습니다.', 'success')
    return redirect(url_for('manager'))


@app.route('/us', methods=['GET'])
def aboutUs():
    return render_template("aboutus/us.html", active_tab='aboutus_tab', title='ABOUT US')


@app.route('/epilogue', methods=['GET'])
def epilogue():
    return render_template("epilogue.html", active_tab='epilogue_tab')


@app.route('/humans/thumbnail', methods=['GET'])
def humans_thumbnail():
    return render_template("thumbnail.html", active_tab='humans_tab')


@app.route('/ajou/thumbnail', methods=['GET'])
def ajou_thumbnail():
    return render_template("thumbnail.html", active_tab='ajou_tab')


@app.route('/upload', methods=['GET'])
def upload():
    return render_template("upload_forms.html", active_tab='ajou_tab')


@app.route('/photo/get/<path:blob_key>/', methods=['GET'])
def photo_get(blob_key):
    if blob_key:
        blob_info = blobstore.get(blob_key)
        logging.warn(blob_info)
        if blob_info:
            img = images.Image(blob_key=blob_key)
            img.im_feeling_lucky()
            thumbnail = img.execute_transforms(output_encoding=images.PNG)

            response = make_response(thumbnail)
            response.headers['Content-Type'] = blob_info.content_type
            return response


@app.route('/photo/resized/<path:blob_key>/', methods=['GET'])
def photo_get_resized(blob_key):
    if blob_key:
        blob_info = blobstore.get(blob_key)
        logging.warn(blob_info)
        if blob_info:
            img = images.Image(blob_key=blob_key)
            img.resize(width=800, height=800)
            img.im_feeling_lucky()
            thumbnail = img.execute_transforms(output_encoding=images.PNG)

            response = make_response(thumbnail)
            response.headers['Content-Type'] = blob_info.content_type
            return response