

from django.urls import path

from myapp import views

urlpatterns = [

    path('',views.login),
    path('logout',views.logout),
    path('adminhome',views.adminhome),
    path('sent_notification',views.sent_notification),
    path('admin_view_notification',views.admin_view_notification),
    path('admin_change_password',views.admin_change_password),
    path('admin_add_owner',views.admin_add_owner),
    path('admin_view_owner',views.admin_view_owner),
    path('admin_view_property',views.admin_view_property),
    path('admin_view_complaints',views.admin_view_complaints),
    path('admin_edit_owner_post',views.admin_edit_owner_post),
    path('delete_owner/<id>',views.delete_owner),
    path('admin_edit_owner/<id>',views.admin_edit_owner),
    path('sendreply/<id>',views.sendreply),
    path('approve_property/<id>',views.approve_property),
    path('reject_property/<id>',views.reject_property),

    path('owner_home', views.owner_home),
    path('add_property', views.add_property),
    path('owner_view_propery', views.owner_view_propery),
    path('owner_viewprofile', views.owner_viewprofile),
    path('onwer_view_booking', views.onwer_view_booking),
    path('approve_booking/<id>', views.approve_booking),
    path('reject_booking/<id>', views.reject_booking),
    path('onwer_view_property_rating/<id>', views.onwer_view_property_rating),
    path('owner_update_property/<id>', views.owner_update_property),
    path('owner_update_property_post', views.owner_update_property_post),

    path('user_reg', views.user_reg),
    path('user_viewprofile', views.user_view_profile),
    path('user_home', views.user_home),
    path('user_edit_profile', views.user_edit_profile),
    path('user_edit_profile_post', views.user_edit_profile_post),
    path('user_view_property', views.user_view_property),
    path('user_send_rating/<id>', views.user_send_rating),
    path('user_book_property/<id>', views.user_book_property),
    path('user_send_rating_post', views.user_send_rating_post),
    path('user_view_booking', views.user_view_booking),
    path('user_view_notification', views.user_view_notification),
    path('sent_complaint', views.sent_complaint),


    # owner chat with user through booking
    path('owner_chat_to_user/<id>', views.owner_chat_to_user),
    path('chat_view', views.chat_view),
    path('chat_send/<msg>', views.chat_send),

    path('user_chat1/<id>', views.user_chat1),
    path('userchat_view', views.userchat_view),
    path('userchat_send/<msg>', views.userchat_send),

]

