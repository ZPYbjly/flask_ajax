from flask import Flask
from apps.views.fire import fire_bp
from apps.views.fireid import fireid_bp
from apps.views.login import login_bp
from setting import DevelopmentConfig
def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(DevelopmentConfig)

    #注册蓝图
    app.register_blueprint(fireid_bp)
    app.register_blueprint(fire_bp)
    app.register_blueprint(login_bp)
    
    return app