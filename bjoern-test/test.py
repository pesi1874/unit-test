#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import bjoern
from flask_app import app


bjoern.run(app, '0.0.0.0', 8002)