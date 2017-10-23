var gulp = require('gulp'),
    cleanCSS = require('gulp-clean-css'),
	notify = require("gulp-notify"),
	plumber = require('gulp-plumber'),
	sass = require('gulp-sass'),
    uglify = require('gulp-uglify'),
    prefix = require('gulp-autoprefixer');

var onError = function(err) {
  notify.onError({
    title:    "Gulp",
    subtitle: "Failure!",
    message:  "Error: <%= error.message %>",
    sound:    "Beep",
    onLast:   true
  })(err);
  this.emit('end');
};

gulp.task('sass', function () {
    gulp.src('./bootstrap/scss/*.scss')
        .pipe(plumber({errorHandler: onError}))
        .pipe(sass().on('error', onError))
        .pipe(prefix({ browsers: ['last 2 versions', '> 10%'] } ))
        .pipe(gulp.dest('core/static/core'))
        .pipe(notify({
          title   : 'Sassification',
          message : 'Styles have been compiled',
          onLast  : true
        }));
});

gulp.task('minify', function() {
  return gulp.src('core/static/core/*.css')
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('css'));
});

gulp.task('watch', function () {
    gulp.watch('./bootstrap/scss/*.scss', ['sass']);
    //gulp.watch('images/icons/*.svg', ['icons']);
    //gulp.watch('js/src/*.js', ['uglify']);
});

gulp.task('default', ['sass', 'watch']);