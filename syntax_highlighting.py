import sublime, sublime_plugin
import os

class DetectFileTypeCommand(sublime_plugin.EventListener):
  """ Detects current file type if the file's extension isn't conclusive """
  """ Modified for Ruby on Rails and Sublime Text 2 """
  """ Original pastie here: http://pastie.org/private/kz8gtts0cjcvkec0d4quqa """

  def on_load(self, view):
    filename = view.file_name()
    if not filename: # buffer has never been saved
      return

    name = os.path.basename(filename.lower())
    if name[-8:] == "_spec.rb":
      # set_syntax(view, "RSpec", "RSpec")
      set_syntax(view, "Ruby on Rails", "Rails")
    elif name == "factories.rb":
      set_syntax(view, "RSpec", "RSpec")
    elif name == "gemfile" or name == "berksfile" or name == "vagrantfile":
      set_syntax(view, "Ruby on Rails", "Rails")
    elif name == "guardfile":
      set_syntax(view, "Ruby on Rails", "Rails")
    elif name[-3:] == ".rb" or name[-3:] == ".ru" or name[-5:] == ".pill" or name[-9:] == ".jbuilder" or name[-10:] == ".jpbuilder" or name[-5:] == ".rabl":
      set_syntax(view, "Ruby on Rails", "Rails")
    elif name[-8:] == ".css.erb":
      set_syntax(view, "CSS", "CSS")
    elif name[-7:] == ".sh.erb":
      set_syntax(view, "Shell-Unix-Generic", "ShellScript")
    # elif name[-9:] == ".scss.erb" or name[-5:] == ".scss":
    #   set_syntax(view, "SCSS", "SCSS")


def set_syntax(view, syntax, path=None):
  if path is None:
    path = syntax
  view.settings().set('syntax', 'Packages/'+ path + '/' + syntax + '.tmLanguage')
  print "Switched syntax to: " + syntax