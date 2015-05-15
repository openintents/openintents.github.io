module Jekyll
  module Titleize

    def titleize(text)
      "#{text.split(' ').each{|word| word.capitalize!}.join('')}"
    end

  end
end

Liquid::Template.register_filter(Jekyll::Titleize)