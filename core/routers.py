from controllers.users.users import router as user_router

routers = [
   {
      'router':user_router,
      'prefix':'/users',
   },
]