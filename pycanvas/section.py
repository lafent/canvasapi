from canvas_object import CanvasObject
from paginated_list import PaginatedList
from util import combine_kwargs


class Section(CanvasObject):

    def __str__(self):
        return 'Section #%s \"%s\" |course_id: %s' % (
            self.id,
            self.name,
            self.course_id
        )

    def get_enrollments(self, **kwargs):
        """
        List all of the enrollments for the current user.

        :calls: `GET /api/v1/sections/:section_id/enrollments \
        <https://canvas.instructure.com/doc/api/enrollments.html#method.enrollments_api.index>`_

        :rtype: :class:`pycanvas.paginated_list.PaginatedList` of :class:`pycanvas.enrollment.Enrollment`
        """
        from enrollment import Enrollment

        return PaginatedList(
            Enrollment,
            self._requester,
            'GET',
            'sections/%s/enrollments' % (self.id),
            **combine_kwargs(**kwargs)
        )

    #Need help
    def cross_list_section(self):
        """
        Move the Section to another course.

        :calls: `POST /api/v1/sections/:id/crosslist/:new_course_id
        \
        <https://canvas.instructure.com/doc/api/sections.html#method.sections.crosslist>`_

        :rtype: :class:`pycanvas.section.Section`
        """
        from course import Course
        response = self._requester.request(
            'POST',
            'sections/%s/crosslist/%s'
        )
    #Need help
    def decross_list_section(self):
        """
        Undo cross-listing of a section.

        :calls: `DELETE /api/v1/sections/:id/crosslist \
        <https://canvas.instructure.com/doc/api/sections.html#method.sections.uncrosslist>`_

        :rtype: :class:`pycanvas.section.Section`
        """
        response = self._requester.request(
            "DELETE",
            "sections/%s/crosslist" % (self.id)
        )
        return Section(self._requester, response.json())

    def edit(self):
        """
        Edit contents of a target section.

        :calls: `PUT /api/v1/sections/:id \
        <https://canvas.instructure.com/doc/api/sections.html#method.sections.update>`_

        :rtype: :class:`pycanvas.section.Section`
        """
        response = self._requester.request(
            "PUT",
            "sections/%s" % (self.id)
        )
        return Section(self._requester, response.json())

    def delete(self):
        """
        Delete a target section.

        :calls: `DELETE /api/v1/sections/:id \
        <https://canvas.instructure.com/doc/api/sections.html#method.sections.destroy>`_

        :rtype: :class:`pycanvas.section.Section`
        """
        response = self._requester.request(
            "DELETE",
            "sections/%s" % (self.id)
        )
        return Section(self._requester, response.json())
