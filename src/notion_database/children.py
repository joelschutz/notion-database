import notion_database.color as clr

class Children:
    def __init__(self):
        """
        init
        """
        self.result = []

    def set_paragraph(self, text=None, color=clr.DEFAULT):
        """
        paragraph configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_heading_1(self, text=None, color=clr.DEFAULT):
        """
        heading_1 configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_heading_2(self, text=None, color=clr.DEFAULT):
        """
        heading_2 configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_heading_3(self, text=None, color=clr.DEFAULT):
        """
        heading_3 configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "heading_3",
            "heading_3": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_callout(self, text=None, color=clr.DEFAULT):
        """
        callout configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "callout",
            "callout": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_quote(self, text=None, color=clr.DEFAULT):
        """
        quote configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "quote",
            "quote": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_bulleted_list_item(self, text=None, color=clr.DEFAULT):
        """
        bulleted_list_item configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_numbered_list_item(self, text=None, color=clr.DEFAULT):
        """
        numbered_list_item configuration

        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "numbered_list_item",
            "numbered_list_item": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        })

    def set_to_do(self, text=None, checked=False, color=clr.DEFAULT):
        """
        to_do configuration

        :param checked:
        :param text: children text.
        :param color: block color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "to_do",
            "to_do": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ],
                "checked": checked,
            }
        })

    def set_toggle(self, text=None, children_text="", color=clr.DEFAULT, children_color=clr.DEFAULT):
        """
        toggle configuration

        :param children_text:
        :param text: children text.
        :param color: block color.
        :param children_color: children color.
        :return:
        """
        if not text:
            text = ""

        self.result.append({
            "object": "block",
            "type": "toggle",
            "toggle": {
                "color":color,
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ],
                "children": [{
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "color":children_color,
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": children_text
                                }
                            }
                        ]
                    }
                }],
            }
        })

    def set_code(self, code=None, lang="plain text"):
        """
        code configuration

        :param lang: language
        :param code: children code.
        :return:
        """
        if not code:
            code = ""

        self.result.append({
            "object": "block",
            "type": "code",
            "code": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": code
                        }
                    }
                ],
                "language": lang,
            }
        })

    def set_embed(self, url=None):
        """
        embed configuration

        :param url: children url.
        :return:
        """
        if not url:
            url = ""

        self.result.append({
            "object": "block",
            "type": "embed",
            "embed": {
                "url": url
            }
        })

    def set_external_image(self, url=None):
        """
        external image configuration

        :param url: children url.
        :return:
        """
        if not url:
            url = ""

        self.result.append({
            "object": "block",
            "type": "image",
            "image": {
                "type": "external",
                "external": {
                    "url": url
                }
            }
        })

    def set_external_video(self, url=None):
        """
        external video configuration

        :param url: children url.
        :return:
        """
        if not url:
            url = ""

        self.result.append({
            "object": "block",
            "type": "video",
            "video": {
                "type": "external",
                "external": {
                    "url": url
                }
            }
        })

    def set_external_file(self, url=None):
        """
        external file configuration

        :param url: children url.
        :return:
        """
        if not url:
            url = ""

        self.result.append({
            "object": "block",
            "type": "file",
            "file": {
                "type": "external",
                "external": {
                    "url": url
                }
            }
        })

    def set_external_pdf(self, url=None):
        """
        external pdf configuration

        :param url: children url.
        :return:
        """
        if not url:
            url = ""

        self.result.append({
            "object": "block",
            "type": "pdf",
            "pdf": {
                "type": "external",
                "external": {
                    "url": url
                }
            }
        })

    def set_bookmark(self, url=None):
        """
        bookmark configuration

        :param url: children url.
        :return:
        """
        if not url:
            url = ""

        self.result.append({
            "object": "block",
            "type": "bookmark",
            "bookmark": {
                "url": url
            }
        })

    def set_equation(self, exp=None):
        """
        equation configuration

        :param exp: children expression.
        :return:
        """
        if not exp:
            exp = ""

        self.result.append({
            "object": "block",
            "type": "equation",
            "equation": {
                "expression": exp
            }
        })

    def set_divider(self):
        """
        divider configuration

        :return:
        """

        self.result.append({
            "object": "block",
            "type": "divider",
            "divider": {}
        })

    def set_table_of_contents(self, color=clr.DEFAULT):
        """
        table_of_contents configuration

        :param color: block color.
        :return:
        """

        self.result.append({
            "object": "block",
            "type": "table_of_contents",
            "table_of_contents": {"color":color}
        })

    def set_breadcrumb(self):
        """
        breadcrumb configuration

        :return:
        """

        self.result.append({
            "object": "block",
            "type": "breadcrumb",
            "breadcrumb": {}
        })

    def clear(self):
        """
        Clear result

        :return:
        """
        self.result.clear()
