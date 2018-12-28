module.exports = function (grunt) {
    'use strict';
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        // we could just concatenate everything, really
        // but we like to have it the complex way.
        // also, in this way we do not have to worry
        // about putting files in the correct order
        // (the dependency tree is walked by r.js)
        less: {
            dist: {
                options: {
                    plugins: [
                        new require('less-plugin-inline-urls'),
                        new require('less-plugin-inline-svg')
                    ],
                    paths: [],
                    strictMath: false,
                    sourceMap: true,
                    outputSourceFiles: true,
                    compress: true,
                    sourceMapURL: '++theme++castle.theme/css/build-compiled.css.map',
                    sourceMapFilename: 'castle/theme/theme_resources/css/build-compiled.css.map',
                    modifyVars: {
                        "isPlone": "false"
                    }
                },
                files: {
                    'castle/theme/theme_resources/css/plone.css': 'castle/theme/theme_resources/css/plone.less',
                    'castle/theme/theme_resources/css/theme.css': 'castle/theme/theme_resources/css/theme.less',
                    'castle/theme/theme_resources/css/frontpage.css': 'castle/theme/theme_resources/css/frontpage.less',
                }
            }
        },

        watch: {
            scripts: {
                files: [
                    'castle/theme/theme_resources/css/*.less',
                    'castle/theme/theme_resources/css/components/*.less'
                ],
                tasks: ['less']
            }
        },
        browserSync: {
            html: {
                bsFiles: {
                    src : ['castle/theme/theme_resources/css/*.less']
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    server: {
                        baseDir: "."
                    },
                }
            },
            plone: {
                bsFiles: {
                    src : ['castle/theme/theme_resources/css/*.less']
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    proxy: "localhost:8080"
                }
            }
        }
    });

    // grunt.loadTasks('tasks');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-sed');
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('build', ['less']);
    grunt.registerTask('bsync', ["browserSync:html", "watch"]);
    grunt.registerTask('plone-bsync', ["browserSync:plone", "watch"]);
};
