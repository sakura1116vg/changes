    return mercurial.parsed_version >= pkg_resources.parse_version('2.4')
        assert vcs.get_default_revision() == 'default'
        revisions = list(vcs.log(offset=0, limit=1))
        assert len(revisions) == 1
        assert revisions[0].subject == 'biz'

        revisions = list(vcs.log(offset=1, limit=1))
        assert len(revisions) == 1
        assert revisions[0].subject == 'test'

    def test_is_child_parent(self):
        vcs = self.get_vcs()
        vcs.clone()
        vcs.update()
        revisions = list(vcs.log())
        assert vcs.is_child_parent(child_in_question=revisions[0].id,
                                   parent_in_question=revisions[1].id)
        assert vcs.is_child_parent(child_in_question=revisions[1].id,
                                   parent_in_question=revisions[0].id) is False