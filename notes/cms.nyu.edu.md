# cms.nyu.edu

Interesting stack trace, no version exposed?

- tried some basic XSS things


Why is this forbidden but other is not found? Possible injection with Sling?
- https://cms.nyu.edu/;%3Cimg%20src=a
- https://cms.nyu.edu/;%3Cimg

## Exposed Sling Things
- https://cms.nyu.edu/system/sling/cqform/defaultlogin.html
- https://cms.nyu.edu/system/sling/info.sessionInfo.txt


```
Forbidden

Cannot serve request to / in org.apache.sling.servlets.get.DefaultGetServlet
Request Progress:

      0 TIMER_START{Request Processing}
      0 COMMENT timer_end format is {<elapsed microseconds>,<timer name>} <optional message>
      4 LOG Method=GET, PathInfo=null
      4 TIMER_START{handleSecurity}
   2117 TIMER_END{2111,handleSecurity} authenticator org.apache.sling.auth.core.impl.SlingAuthenticator@7332ed47 returns true
   2325 TIMER_START{ResourceResolution}
   3579 TIMER_END{1252,ResourceResolution} URI=/ resolves to Resource=JcrNodeResource, type=cq:Page, superType=null, path=/etc/designs/nyu
   3582 LOG Resource Path Info: SlingRequestPathInfo: path='/etc/designs/nyu', selectorString='null', extension='null', suffix='/'
   3583 TIMER_START{ServletResolution}
   3584 TIMER_START{resolveServlet(/etc/designs/nyu)}
   3592 TIMER_END{7,resolveServlet(/etc/designs/nyu)} Using servlet org.apache.sling.servlets.get.DefaultGetServlet
   3594 TIMER_END{10,ServletResolution} URI=/ handled by Servlet=org.apache.sling.servlets.get.DefaultGetServlet
   3596 LOG Applying Requestfilters
   3601 LOG Calling filter: com.adobe.granite.resourceresolverhelper.impl.ResourceResolverHelperImpl
   3604 LOG Calling filter: org.apache.sling.security.impl.ContentDispositionFilter
   3606 LOG Calling filter: com.adobe.granite.csrf.impl.CSRFFilter
   3610 LOG Calling filter: org.apache.sling.i18n.impl.I18NFilter
   3613 LOG Calling filter: com.adobe.granite.httpcache.impl.InnerCacheFilter
   3616 LOG Calling filter: org.apache.sling.rewriter.impl.RewriterFilter
   3618 LOG Calling filter: com.day.cq.wcm.core.impl.WCMRequestFilter
   3623 LOG Calling filter: com.adobe.cq.history.impl.HistoryRequestFilter
   4764 LOG Calling filter: com.adobe.cq.wcm.core.components.internal.servlets.CoreFormHandlingServlet
   4767 LOG Calling filter: com.day.cq.wcm.foundation.forms.impl.FormsHandlingServlet
   4769 LOG Calling filter: com.adobe.granite.optout.impl.OptOutFilter
   4772 LOG Calling filter: com.adobe.cq.social.commons.cors.CORSAuthenticationFilter
   4775 LOG Calling filter: org.apache.sling.engine.impl.debug.RequestProgressTrackerLogFilter
   4779 LOG Calling filter: edu.nyu.aemnyu.core.impl.filters.LoggingFilter
   4781 LOG Calling filter: edu.nyu.aemdental.core.filters.SampleLoggingFilter
   4783 LOG Calling filter: com.day.cq.wcm.mobile.core.impl.redirect.RedirectFilter
   4785 LOG Calling filter: com.day.cq.wcm.core.impl.AuthoringUIModeServiceImpl
   4881 LOG Calling filter: com.adobe.granite.rest.assets.impl.AssetContentDispositionFilter
   4884 LOG Calling filter: com.adobe.granite.requests.logging.impl.RequestLoggerImpl
   4887 LOG Calling filter: com.adobe.granite.rest.impl.servlet.ApiResourceFilter
   4911 LOG Calling filter: com.day.cq.dam.core.impl.servlet.ActivityRecordHandler
   4918 LOG Calling filter: com.adobe.cq.social.ugcbase.security.impl.SaferSlingPostServlet
   4920 LOG Calling filter: com.day.cq.wcm.core.impl.warp.TimeWarpFilter
   4923 LOG Calling filter: com.day.cq.dam.core.impl.assetlinkshare.AdhocAssetShareAuthHandler
   4927 LOG Applying Componentfilters
   4929 LOG Calling filter: com.day.cq.personalization.impl.TargetComponentFilter
   4932 LOG Calling filter: com.day.cq.wcm.core.impl.page.PageLockFilter
   4935 LOG Calling filter: com.day.cq.wcm.core.impl.WCMComponentFilter
   4951 LOG Calling filter: com.day.cq.wcm.core.impl.WCMDebugFilter
   4956 TIMER_START{org.apache.sling.servlets.get.DefaultGetServlet#0}
   4961 LOG Using org.apache.sling.servlets.get.impl.helpers.StreamRenderer to render for extension=null
   4995 LOG Applying Error filters
   4996 LOG Calling filter: org.apache.sling.i18n.impl.I18NFilter
   4997 LOG Calling filter: org.apache.sling.rewriter.impl.RewriterFilter
   5000 TIMER_START{handleError:status=403}
   5418 TIMER_END{417,handleError:status=403} Using handler /libs/sling/servlet/errorhandler/default.jsp
   8640 LOG Found processor for post processing ProcessorConfiguration: {contentTypes=[text/html], order=-1, active=true, valid=true, processErrorResponse=true, pipeline=(generator=Config(type=htmlparser, config={}), transformers=(Config(type=linkchecker, config={}), Config(type=mobile, config=JcrPropertyMap [node=Node[NodeDelegate{tree=/libs/cq/config/rewriter/default/transformer-mobile: { jcr:primaryType = nt:unstructured, component-optional = true}}], values={jcr:primaryType=nt:unstructured, component-optional=true}]), Config(type=mobiledebug, config=JcrPropertyMap [node=Node[NodeDelegate{tree=/libs/cq/config/rewriter/default/transformer-mobiledebug: { jcr:primaryType = nt:unstructured, component-optional = true}}], values={jcr:primaryType=nt:unstructured, component-optional=true}]), Config(type=contentsync, config=JcrPropertyMap [node=Node[NodeDelegate{tree=/libs/cq/config/rewriter/default/transformer-contentsync: { jcr:primaryType = nt:unstructured, component-optional = true}}], values={jcr:primaryType=nt:unstructured, component-optional=true}]), serializer=Config(type=htmlwriter, config={}))}
   8758 TIMER_END{8756,Request Processing} Dumping SlingRequestProgressTracker Entries

Apache Sling
```
