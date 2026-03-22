



<!DOCTYPE html>
<html class="gl-light ui-neutral with-top-bar" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
<title>raise_on_message/__init__.py · master · dan drum / gajim-plugins · GitLab</title>
<script>
//<![CDATA[
window.gon={};gon.math_rendering_limits_enabled=true;gon.features={"inlineBlame":false,"blobOverflowMenu":false};
//]]>
</script>
<script>
//<![CDATA[
window.uploads_path = "/4q1/gajim-plugins/uploads";



//]]>
</script>

<script>
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: [String!]!\n  $ref: String!\n  $refType: RefType\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: $filePath, ref: $ref, refType: $refType) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canModifyBlobWithWebIde\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"4q1/gajim-plugins","ref":"master","refType":null,"filePath":"raise_on_message/__init__.py","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"ES8v7NQ00lZtLaVXaSAJ7E5CzyQjC2HypnjdyAX3noL_O-R-aOLFZOgLT4H7HDZJ1n2P_3nSRRDSwfzYv03lcg","x-gitlab-feature-category":"source_code_management"};
  const url = `https://dev.gajim.org/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.20ee338e.chunk.js">

<link rel="stylesheet" href="/assets/application-24450da7e1f98e29c399d9abbc571023152a547333f2b6a44e6087cb8138e10b.css" />
<link rel="stylesheet" href="/assets/page_bundles/tree-f95f64689d3a4eccbc4fddee3de02a3bd8a3b9c1eb74281404c45e35e63c5f31.css" /><link rel="stylesheet" href="/assets/page_bundles/projects-c98ca5e3f59d8b65f8d41a7a7861d635090af2e1c3ccbae649f650aa7d8535cb.css" /><link rel="stylesheet" href="/assets/page_bundles/commit_description-1e2cba4dda3c7b30dd84924809020c569f1308dea51520fe1dd5d4ce31403195.css" /><link rel="stylesheet" href="/assets/page_bundles/work_items-22a76cdd1fe2ae5431b7ff603f86212acaf81b49c4a932f19e3b3222dc1881ee.css" /><link rel="stylesheet" href="/assets/page_bundles/notes_shared-7e727ab1e91b421915feadeb04a1b9d57213cb1b2f8f56f4d894b34d6b42e9b3.css" />
<link rel="stylesheet" href="/assets/application_utilities-58bec0f2dc46133fc9e8548af9854688398e9d7263cc0fd95ec5739f2a069dec.css" />
<link rel="stylesheet" href="/assets/tailwind-a7ef7f0163fd11f5c5e7d219e045590a4d61325f1d3e37ad339ee77390b5ce51.css" />


<link rel="stylesheet" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" />
<link rel="stylesheet" href="/assets/highlight/themes/white-e31d355458ead69f8798dbb62f54c60c4ccc7db35289cbbd2353ddfdf5109aac.css" />


<link rel="preload" href="/assets/application_utilities-58bec0f2dc46133fc9e8548af9854688398e9d7263cc0fd95ec5739f2a069dec.css" as="style" type="text/css">
<link rel="preload" href="/assets/application-24450da7e1f98e29c399d9abbc571023152a547333f2b6a44e6087cb8138e10b.css" as="style" type="text/css">
<link rel="preload" href="/assets/highlight/themes/white-e31d355458ead69f8798dbb62f54c60c4ccc7db35289cbbd2353ddfdf5109aac.css" as="style" type="text/css">




<script src="/assets/webpack/runtime.0fadbe20.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.8bb7a981.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.abuse_reports.show-pages.admin.topics.edit-pages.admin.topics.new-pages.dashboar-b3f02029.8a5a4d8e.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.abuse_reports.show-pages.dashboard.issues-pages.dashboard.milestones.show-pages.-2aa358ab.17d7df78.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.abuse_reports.show-pages.dashboard.issues-pages.groups.boards-pages.groups.issue-557dc7ac.6ed2f82b.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.abuse_reports.show-pages.dashboard.issues-pages.groups.boards-pages.groups.issue-f4cc8b61.ff8aaaaa.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.new-pages.import.gitlab_projects.new-pages.import.manifest.new-pages.projects.n-44c6c18e.6f9d92a6.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.search.show-super_sidebar.d6a42c57.chunk.js" defer="defer"></script>
<script src="/assets/webpack/super_sidebar.6f6dc099.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-2e472f70.182f2eae.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.branches.new-pages.projects.commits.show-pages.proje-81161c0b.96528f58.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.edit-pages.projects.sni-42df7d4c.edd6a916.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.edit-pages.projects.blob.new-pages.projects.blob.show-pages.projects.for-70061bf1.29e2b13e.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.b59c1abb.chunk.js" defer="defer"></script>
<script src="/assets/webpack/106.d0a09673.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.branches.index-pages.projects.show-pages.projects.ta-c9380b86.704c7428.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.show-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.eb9e9de2.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.shared.web_ide_link-pages.projects.show-pages.projec-cf300cc3.60d10c26.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.f4c3db17.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.tree.show-treeList.a071dbe2.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.0321409d.chunk.js" defer="defer"></script>

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="raise_on_message/__init__.py · master · dan drum / gajim-plugins · GitLab" property="og:title">
<meta content="Plugins developed for Gajim XMPP client. This is a community effort." property="og:description">
<meta content="https://dev.gajim.org/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://dev.gajim.org/4q1/gajim-plugins/-/blob/master/raise_on_message/__init__.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="raise_on_message/__init__.py · master · dan drum / gajim-plugins · GitLab" property="twitter:title">
<meta content="Plugins developed for Gajim XMPP client. This is a community effort." property="twitter:description">
<meta content="https://dev.gajim.org/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="fbOIqKji75PzmO6Yo57yBZSlZxU_qMy1o5jZMfoSROKTp0M6FDT4oXa-BE4xos2gDJonzmVx6FfXIfghQKg_Eg" />
<meta name="csp-nonce" />
<meta name="action-cable-url" content="/-/cable" />
<link href="/-/manifest.json" rel="manifest">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




<meta content="Plugins developed for Gajim XMPP client. This is a community effort." name="description">
<meta content="#ececef" name="theme-color">
</head>

<body class="tab-width-8 gl-browser-firefox gl-platform-windows" data-namespace-id="51989" data-page="projects:blob:show" data-page-type-id="master/raise_on_message/__init__.py" data-project="gajim-plugins" data-project-full-path="4q1/gajim-plugins" data-project-id="418">

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isFirefox":true,"isWindows":true};


//]]>
</script>


<div class="layout-page page-with-super-sidebar">
<aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/4q1/gajim-plugins/-/files/master?format=json&quot;,&quot;project_blob_url&quot;:&quot;/4q1/gajim-plugins/-/blob/master&quot;}" data-force-desktop-expanded-sidebar="" data-is-saas="false" data-root-path="/" data-sidebar="{&quot;whats_new_most_recent_release_items_count&quot;:6,&quot;whats_new_version_digest&quot;:&quot;c955dbe1b30a1468b032fe6896086eda50f884ff9559d966e5ef75c34eee3ff0&quot;,&quot;is_logged_in&quot;:true,&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Your work&quot;,&quot;link&quot;:&quot;/&quot;,&quot;icon&quot;:&quot;work&quot;},{&quot;title&quot;:&quot;Explore&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;},{&quot;title&quot;:&quot;Profile&quot;,&quot;link&quot;:&quot;/-/user_settings/profile&quot;,&quot;icon&quot;:&quot;profile&quot;},{&quot;title&quot;:&quot;Preferences&quot;,&quot;link&quot;:&quot;/-/profile/preferences&quot;,&quot;icon&quot;:&quot;preferences&quot;}],&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;gajim-plugins&quot;,&quot;entity_id&quot;:418,&quot;link&quot;:&quot;/4q1/gajim-plugins&quot;,&quot;link_classes&quot;:&quot;shortcuts-project&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;manage_menu&quot;,&quot;title&quot;:&quot;Manage&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/activity&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/activity&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Members&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/project_members&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/labels&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;plan_menu&quot;,&quot;title&quot;:&quot;Plan&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/issues&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Issues&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/issues&quot;,&quot;pill_count_field&quot;:&quot;openIssuesCount&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Issue boards&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/boards&quot;,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/milestones&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/wikis/home&quot;,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;code_menu&quot;,&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/merge_requests&quot;,&quot;pill_count_field&quot;:&quot;openMergeRequestsCount&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/tree/master&quot;,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/branches&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Commits&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/commits/master?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Tags&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/tags&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Repository graph&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/network/master?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Compare revisions&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/compare?from=master\u0026to=master&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;build_menu&quot;,&quot;title&quot;:&quot;Build&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/pipelines&quot;,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/jobs&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipelines_editor&quot;,&quot;title&quot;:&quot;Pipeline editor&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/ci/editor?branch_name=master&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Pipeline schedules&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/pipeline_schedules&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artifacts&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/artifacts&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;secure_menu&quot;,&quot;title&quot;:&quot;Secure&quot;,&quot;icon&quot;:&quot;shield&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/security/configuration&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;configuration&quot;,&quot;title&quot;:&quot;Security configuration&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/security/configuration&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;deploy_menu&quot;,&quot;title&quot;:&quot;Deploy&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/releases&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/releases&quot;,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;feature_flags&quot;,&quot;title&quot;:&quot;Feature flags&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/feature_flags&quot;,&quot;link_classes&quot;:&quot;shortcuts-feature-flags&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Package Registry&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/packages&quot;,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_registry&quot;,&quot;title&quot;:&quot;Model registry&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/ml/models&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pages&quot;,&quot;title&quot;:&quot;Pages&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/pages&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;operations_menu&quot;,&quot;title&quot;:&quot;Operate&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/environments&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environments&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/environments&quot;,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;kubernetes&quot;,&quot;title&quot;:&quot;Kubernetes clusters&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/clusters&quot;,&quot;link_classes&quot;:&quot;shortcuts-kubernetes&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;terraform_states&quot;,&quot;title&quot;:&quot;Terraform states&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/terraform&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Terraform modules&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/terraform_module_registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;google_cloud&quot;,&quot;title&quot;:&quot;Google Cloud&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/google_cloud/configuration&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;monitor_menu&quot;,&quot;title&quot;:&quot;Monitor&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/error_tracking&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;error_tracking&quot;,&quot;title&quot;:&quot;Error Tracking&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/error_tracking&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;alert_management&quot;,&quot;title&quot;:&quot;Alerts&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/alert_management&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/incidents&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;analyze_menu&quot;,&quot;title&quot;:&quot;Analyze&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Value stream analytics&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/value_stream_analytics&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor analytics&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/graphs/master?ref_type=heads&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;CI/CD analytics&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/pipelines/charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Repository analytics&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/graphs/master/charts&quot;,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Model experiments&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/ml/experiments&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;settings_menu&quot;,&quot;title&quot;:&quot;Settings&quot;,&quot;icon&quot;:&quot;settings&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/edit&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;general&quot;,&quot;title&quot;:&quot;General&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/edit&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;integrations&quot;,&quot;title&quot;:&quot;Integrations&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/integrations&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;webhooks&quot;,&quot;title&quot;:&quot;Webhooks&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/hooks&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;access_tokens&quot;,&quot;title&quot;:&quot;Access tokens&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/access_tokens&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/repository&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;merge_request_settings&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/merge_requests&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd&quot;,&quot;title&quot;:&quot;CI/CD&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/ci_cd&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_and_registries&quot;,&quot;title&quot;:&quot;Packages and registries&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/packages_and_registries&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;monitor&quot;,&quot;title&quot;:&quot;Monitor&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/settings/operations&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;usage_quotas&quot;,&quot;title&quot;:&quot;Usage Quotas&quot;,&quot;link&quot;:&quot;/4q1/gajim-plugins/-/usage_quotas&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:true}],&quot;current_context_header&quot;:&quot;Project&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;docs_path&quot;:&quot;/help/docs&quot;,&quot;display_whats_new&quot;:true,&quot;show_version_check&quot;:false,&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;settings_path&quot;:&quot;/search/settings&quot;,&quot;search_context&quot;:{&quot;project&quot;:{&quot;id&quot;:418,&quot;name&quot;:&quot;gajim-plugins&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/4q1/gajim-plugins/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/4q1/gajim-plugins/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;master&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;panel_type&quot;:&quot;project&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Milestones&quot;,&quot;href&quot;:&quot;/dashboard/milestones&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-milestones&quot;},{&quot;title&quot;:&quot;Snippets&quot;,&quot;href&quot;:&quot;/dashboard/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Activity&quot;,&quot;href&quot;:&quot;/dashboard/activity&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-activity&quot;},{&quot;title&quot;:&quot;Groups&quot;,&quot;href&quot;:&quot;/dashboard/groups&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;},{&quot;title&quot;:&quot;Projects&quot;,&quot;href&quot;:&quot;/dashboard/projects&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;},{&quot;title&quot;:&quot;Create a new issue&quot;,&quot;href&quot;:&quot;/4q1/gajim-plugins/-/issues/new&quot;,&quot;css_class&quot;:&quot;shortcuts-new-issue&quot;}],&quot;terms&quot;:null,&quot;is_admin&quot;:false,&quot;name&quot;:&quot;dan drum&quot;,&quot;username&quot;:&quot;4q1&quot;,&quot;admin_url&quot;:&quot;https://dev.gajim.org/admin&quot;,&quot;admin_mode&quot;:{&quot;admin_mode_feature_enabled&quot;:false,&quot;admin_mode_active&quot;:false,&quot;enter_admin_mode_url&quot;:&quot;/admin/session/new&quot;,&quot;leave_admin_mode_url&quot;:&quot;/admin/session/destroy&quot;,&quot;user_is_admin&quot;:false},&quot;avatar_url&quot;:null,&quot;has_link_to_profile&quot;:true,&quot;link_to_profile&quot;:&quot;/4q1&quot;,&quot;logo_url&quot;:null,&quot;status&quot;:{&quot;can_update&quot;:true,&quot;busy&quot;:null,&quot;customized&quot;:null,&quot;availability&quot;:&quot;&quot;,&quot;emoji&quot;:null,&quot;message_html&quot;:null,&quot;message&quot;:null,&quot;clear_after&quot;:null},&quot;settings&quot;:{&quot;has_settings&quot;:true,&quot;profile_path&quot;:&quot;/-/user_settings/profile&quot;,&quot;profile_preferences_path&quot;:&quot;/-/profile/preferences&quot;},&quot;user_counts&quot;:{&quot;assigned_issues&quot;:0,&quot;assigned_merge_requests&quot;:0,&quot;review_requested_merge_requests&quot;:0,&quot;todos&quot;:1,&quot;last_update&quot;:1774141790199},&quot;can_sign_out&quot;:true,&quot;sign_out_link&quot;:&quot;/users/sign_out&quot;,&quot;issues_dashboard_path&quot;:&quot;/dashboard/issues?assignee_username=4q1&quot;,&quot;merge_request_dashboard_path&quot;:null,&quot;todos_dashboard_path&quot;:&quot;/dashboard/todos&quot;,&quot;create_new_menu_groups&quot;:[{&quot;name&quot;:&quot;In this project&quot;,&quot;items&quot;:[{&quot;text&quot;:&quot;New issue&quot;,&quot;href&quot;:&quot;/4q1/gajim-plugins/-/issues/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;new_issue&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;new_issue&quot;}},{&quot;text&quot;:&quot;New merge request&quot;,&quot;href&quot;:&quot;/4q1/gajim-plugins/-/merge_requests/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;new_mr&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;new_mr&quot;}},{&quot;text&quot;:&quot;Invite members&quot;,&quot;href&quot;:null,&quot;component&quot;:&quot;invite_members&quot;,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;invite&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;invite&quot;}}]},{&quot;name&quot;:&quot;In GitLab&quot;,&quot;items&quot;:[{&quot;text&quot;:&quot;New project/repository&quot;,&quot;href&quot;:&quot;/projects/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;general_new_project&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;general_new_project&quot;}},{&quot;text&quot;:&quot;New snippet&quot;,&quot;href&quot;:&quot;/-/snippets/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;general_new_snippet&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;general_new_snippet&quot;}}]}],&quot;merge_request_menu&quot;:[{&quot;name&quot;:&quot;Merge requests&quot;,&quot;items&quot;:[{&quot;text&quot;:&quot;Assigned&quot;,&quot;href&quot;:&quot;/dashboard/merge_requests?assignee_username=4q1&quot;,&quot;count&quot;:0,&quot;userCount&quot;:&quot;assigned_merge_requests&quot;,&quot;extraAttrs&quot;:{&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-label&quot;:&quot;merge_requests_assigned&quot;,&quot;data-track-property&quot;:&quot;nav_core_menu&quot;,&quot;class&quot;:&quot;dashboard-shortcuts-merge_requests&quot;}},{&quot;text&quot;:&quot;Review requests&quot;,&quot;href&quot;:&quot;/dashboard/merge_requests?reviewer_username=4q1&quot;,&quot;count&quot;:0,&quot;userCount&quot;:&quot;review_requested_merge_requests&quot;,&quot;extraAttrs&quot;:{&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-label&quot;:&quot;merge_requests_to_review&quot;,&quot;data-track-property&quot;:&quot;nav_core_menu&quot;,&quot;class&quot;:&quot;dashboard-shortcuts-review_requests&quot;}}]}],&quot;projects_path&quot;:&quot;/dashboard/projects&quot;,&quot;groups_path&quot;:&quot;/dashboard/groups&quot;,&quot;gitlab_com_but_not_canary&quot;:false,&quot;gitlab_com_and_canary&quot;:false,&quot;canary_toggle_com_url&quot;:&quot;https://next.gitlab.com&quot;,&quot;current_context&quot;:{&quot;namespace&quot;:&quot;projects&quot;,&quot;item&quot;:{&quot;id&quot;:418,&quot;name&quot;:&quot;gajim-plugins&quot;,&quot;namespace&quot;:&quot;dan drum / gajim-plugins&quot;,&quot;fullPath&quot;:&quot;4q1/gajim-plugins&quot;,&quot;webUrl&quot;:&quot;/4q1/gajim-plugins&quot;,&quot;avatarUrl&quot;:null}},&quot;pinned_items&quot;:[&quot;project_issue_list&quot;,&quot;project_merge_request_list&quot;],&quot;update_pins_url&quot;:&quot;/-/users/pins&quot;,&quot;is_impersonating&quot;:false,&quot;stop_impersonation_path&quot;:&quot;/admin/impersonation&quot;,&quot;track_visits_path&quot;:&quot;/-/track_namespace_visits&quot;,&quot;work_items&quot;:null}"></aside>

<div class="content-wrapper">
<div class="broadcast-wrapper">




</div>
<div class="alert-wrapper alert-wrapper-top-space gl-flex gl-flex-col gl-gap-3 container-fluid container-limited">

























</div>
<div class="top-bar-fixed container-fluid" data-testid="top-bar">
<div class="top-bar-container gl-flex gl-items-center gl-gap-2">
<div class="gl-grow gl-basis-0 gl-flex gl-items-center gl-justify-start">
<button class="gl-button btn btn-icon btn-md btn-default btn-default-tertiary js-super-sidebar-toggle-expand super-sidebar-toggle -gl-ml-3" aria-controls="super-sidebar" aria-expanded="false" aria-label="Primary navigation sidebar" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="sidebar-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#sidebar"></use></svg>

</button>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"dan drum","item":"https://dev.gajim.org/4q1"},{"@type":"ListItem","position":2,"name":"gajim-plugins","item":"https://dev.gajim.org/4q1/gajim-plugins"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://dev.gajim.org/4q1/gajim-plugins/-/blob/master/raise_on_message/__init__.py"}]}


</script>
<div data-testid="breadcrumb-links" id="js-vue-page-breadcrumbs-wrapper">
<div data-breadcrumbs-json="[{&quot;text&quot;:&quot;dan drum&quot;,&quot;href&quot;:&quot;/4q1&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;gajim-plugins&quot;,&quot;href&quot;:&quot;/4q1/gajim-plugins&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;Repository&quot;,&quot;href&quot;:&quot;/4q1/gajim-plugins/-/blob/master/raise_on_message/__init__.py&quot;,&quot;avatarPath&quot;:null}]" id="js-vue-page-breadcrumbs"></div>
<div id="js-injected-page-breadcrumbs"></div>
</div>


</div>
<div class="gl-flex-none gl-flex gl-items-center gl-justify-center">
<div id="js-advanced-search-modal"></div>

</div>
<div class="gl-grow gl-basis-0 gl-flex gl-items-center gl-justify-end">
<div id="js-work-item-feedback"></div>


</div>
</div>
</div>

<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-testid="flash-container">
<div id="js-global-alerts"></div>
</div>


<div class="js-invite-members-modal" data-access-levels="{&quot;Guest&quot;:10,&quot;Planner&quot;:15,&quot;Reporter&quot;:20,&quot;Developer&quot;:30,&quot;Maintainer&quot;:40,&quot;Owner&quot;:50}" data-default-access-level="10" data-full-path="4q1/gajim-plugins" data-help-link="https://dev.gajim.org/help/user/permissions.md" data-id="418" data-is-project="true" data-name="gajim-plugins" data-reload-page-on-submit="false" data-root-id="51989"></div>




<div class="js-signature-container" data-signatures-path="/4q1/gajim-plugins/-/commits/4ef971e8ffdba9a747058f27c3766be51718e6fe/signatures?limit=1"></div>

<div class="tree-holder gl-pt-4" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder gl-max-w-26">
<div data-project-id="418" data-project-root-path="/4q1/gajim-plugins" data-ref="master" data-ref-type="" id="js-tree-ref-switcher"></div>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/4q1/gajim-plugins/-/tree/master">gajim-plugins
</a></li>
<li class="breadcrumb-item">
<a href="/4q1/gajim-plugins/-/tree/master/raise_on_message">raise_on_message</a>
</li>
<li class="breadcrumb-item">
<a href="/4q1/gajim-plugins/-/blob/master/raise_on_message/__init__.py"><strong>__init__.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-flex gl-flex-wrap sm:gl-flex-nowrap gl-items-baseline gl-gap-3">
<button class="gl-button btn btn-md btn-default has-tooltip shortcuts-find-file" title="Go to file, press &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;/~&lt;/kbd&gt; or &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;t&lt;/kbd&gt;" aria-keyshortcuts="/+~ t" data-html="true" data-event-tracking="click_find_file_button_on_repository_pages" type="button"><span class="gl-button-text">
Find file

</span>

</button>
<a data-event-tracking="click_blame_control_on_blob_page" class="gl-button btn btn-md btn-default js-blob-blame-link" href="/4q1/gajim-plugins/-/blame/master/raise_on_message/__init__.py"><span class="gl-button-text">
Blame
</span>

</a>
<a aria-keyshortcuts="y" class="gl-button btn btn-md btn-default has-tooltip js-data-file-blob-permalink-url" data-html="true" title="Go to permalink &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;y&lt;/kbd&gt;" href="/4q1/gajim-plugins/-/blob/f191367db3392fa89d070781c5472133e3e5a5fa/raise_on_message/__init__.py"><span class="gl-button-text">
Permalink
</span>

</a>
</div>
</div>

<div data-ahead-compare-path="/4q1/gajim-plugins/-/compare/master...master?from_project_id=13" data-behind-compare-path="/gajim/gajim-plugins/-/compare/master...master?from_project_id=418" data-can-sync-branch="true" data-project-path="4q1/gajim-plugins" data-selected-branch="master" data-source-default-branch="master" data-source-name="gajim / gajim-plugins" data-source-path="/gajim/gajim-plugins" data-view-mr-path="/gajim/gajim-plugins/-/merge_requests/233" id="js-fork-info"></div>
<div class="info-well">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-4ef971e8">
<div class="gl-self-start gl-block">
<a href="/4q1"><img alt="dan drum&#39;s avatar" src="/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png" class="avatar s32 gl-inline-block" title="dan drum"></a>
</div>
<div class="commit-detail flex-list gl-flex gl-justify-between gl-items-start gl-grow gl-min-w-0 gl-mb-3">
<div class="commit-content gl-self-center" data-testid="commit-content">
<div class="gl-flex sm:gl-hidden gl-gap-3 gl-items-center">
<div class="committer gl-text-sm">
<time class="js-timeago" title="Mar 14, 2026 2:20am" datetime="2026-03-14T02:20:23Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Mar 14, 2026</time>
</div>
<a class="gl-button btn btn-md btn-link commit-row-message js-onboarding-commit-item" href="/4q1/gajim-plugins/-/commit/4ef971e8ffdba9a747058f27c3766be51718e6fe"><svg class="s16 gl-icon gl-button-icon " data-testid="commit-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#commit"></use></svg>
<span class="gl-button-text">
4ef971e8

</span>

</a></div>
<div class="gl-hidden sm:gl-block">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/4q1/gajim-plugins/-/commit/4ef971e8ffdba9a747058f27c3766be51718e6fe">Upload New File</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
4ef971e8
</span>
<div class="committer gl-text-sm">
<a class="commit-author-link js-user-link" data-user-id="51806" href="/4q1">dan drum</a> authored <time class="js-timeago" title="Mar 14, 2026 2:20am" datetime="2026-03-14T02:20:23Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Mar 14, 2026</time>
</div>


</div>
</div>
<div class="commit-actions gl-flex gl-items-center gl-gap-3">
<div class="gl-hidden sm:gl-flex gl-items-center gl-gap-3">

<div class="js-commit-pipeline-status" data-endpoint="/4q1/gajim-plugins/-/commit/4ef971e8ffdba9a747058f27c3766be51718e6fe/pipelines?ref=master"></div>
<div class="commit-sha-group btn-group gl-hidden sm:gl-flex">
<div class="label label-monospace monospace">
4ef971e8
</div>
<button class="gl-button btn btn-icon btn-md btn-default " title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite" data-toggle="tooltip" data-placement="bottom" data-container="body" data-html="true" data-category="primary" data-size="medium" data-clipboard-text="4ef971e8ffdba9a747058f27c3766be51718e6fe" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="copy-to-clipboard-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#copy-to-clipboard"></use></svg>

</button>

</div>
</div>
<div class="gl-block sm:gl-hidden">
<button class="gl-button btn btn-icon btn-md btn-default button-ellipsis-horizontal text-expander js-toggle-button" data-toggle="tooltip" data-container="body" data-collapse-title="Toggle commit description" data-expand-title="Toggle commit description" title="Toggle commit description" aria-label="Toggle commit description" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="ellipsis_h-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#ellipsis_h"></use></svg>

</button>
</div>
<div data-event-tracking="click_history_control_on_blob_page" data-history-link="/4q1/gajim-plugins/-/commits/master/raise_on_message/__init__.py" id="js-commit-history-link"></div>
</div>
</div>
<div class="gl-block sm:gl-hidden">
<div class="gl-hidden js-toggle-content gl-mt-6">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/4q1/gajim-plugins/-/commit/4ef971e8ffdba9a747058f27c3766be51718e6fe">Upload New File</a>
<div class="committer gl-text-sm">
<a class="commit-author-link js-user-link" data-user-id="51806" href="/4q1">dan drum</a> authored <time class="js-timeago" title="Mar 14, 2026 2:20am" datetime="2026-03-14T02:20:23Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Mar 14, 2026</time>
</div>

</div>
</div>
</li>

</ul>
</div>
<div class="gl-hidden sm:gl-block">

</div>
</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="raise_on_message/__init__.py" data-can-download-code="true" data-original-branch="master" data-project-path="4q1/gajim-plugins" data-ref-type="" data-resource-id="gid://gitlab/Project/418" data-target-branch="master" data-user-id="gid://gitlab/User/51806" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-hidden class="gl-spinner gl-spinner-md gl-spinner-dark !gl-align-text-bottom"></span><span class="gl-sr-only !gl-absolute">Loading</span>
</div>
</div>
</div>

</div>
<script>
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/4q1/gajim-plugins/edit/master/-/raise_on_message/__init__.py'


//]]>
</script>
<div data-ambiguous="false" data-ref="master" id="js-ambiguous-ref-modal"></div>

</main>
</div>


</div>
</div>


<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.testid = 'js-lazy-loaded-content';
  });
}

//]]>
</script>
<script>
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>

