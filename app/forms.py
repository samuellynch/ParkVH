class PostForm(Form):
    post = StringField('post', validatores=[DataRequired()])