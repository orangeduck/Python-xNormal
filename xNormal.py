import os

"""
path: The path to xNormal.exe
version: The version of xNormal installed
config_file: The default name for generated config files 
"""

path = "xNormal.exe"
version = "3.19.3"
config_file = "xNormal.xml"


def run(high_path, low_path, out_path, **opts):
    """ Basic interface to run xNormal using a single high and low poly mesh """
    
    opts["out"] = os.path.abspath(out_path)
    conf = config([high_mesh_options(high_path)], [low_mesh_options(low_path)], generation_options(out_path, **opts))
    return run_config(conf)

    
def run_config(conf):
    """ Runs xNormal using a provided configuration XML string. """
    
    f = open(config_file, 'w')
    f.write(conf)
    f.close()
    
    retcode = os.system("\"%s\" %s" % (path, config_file))
    os.remove(config_file)
    
    return retcode
   
   
def run_config_filename(conf_filename):
    """ Runs xNormal using the path to a configuration file. """
    retcode = os.system("\"%s\" %s" % (path, conf_filename))
    return retcode
    
    
def high_mesh_options(filename, **kwargs):
    """ Generates an options dictionary for a high mesh """
    
    kwargs["path"] = os.path.abspath(filename)
    
    """
    List of possible high mesh options in the form: 
        (keyword_argument, xml_name, default_value)
    """
    high_opts = [
        ("visible", "Visible", True),
        ("scale", "Scale", 1.000000),
        ("ignore_vertex_colors", "IgnorePerVertexColor", True),
        ("average_normals", "AverageNormals", "UseExportedNormals"),
        ("texture_is_normalmap", "BaseTexIsTSNM", False),
        ("path", "File", ""),
        ("position_offset", "PositionOffset", "0.0000;0.0000;0.0000"),
        ("base_texture", "BaseTex", ""),
    ]
    
    def lookup(dict, key, default):
        if key in dict: return dict[key]
        else: return default
    
    high_opts = [(xml, lookup(kwargs, kw, val)) for kw, xml, val in high_opts ]
    
    return high_opts
    
    
def low_mesh_options(filename, **kwargs):
    """ Generates an options dictionary for a low mesh """
    
    kwargs["path"] = os.path.abspath(filename)
    
    """
    List of possible low mesh options in the form: 
        (keyword_argument, xml_name, default_value)
    """
    low_opts = [
        ("visible", "Visible", True),
        ("path", "File", ""),
        ("average_normals", "AverageNormals", "UseExportedNormals"),
        ("forward_ray_dist", "MaxRayDistanceFront", 0.5),
        ("backward_ray_dist", "MaxRayDistanceBack", 0.5),
        ("use_cage", "UseCage", False),
        ("normal_map_type", "NormapMapType", "Tangent-space"),
        ("vertex_colors", "UsePerVertexColors", True),
        ("fresnel", "UseFresnel", False),
        ("fresnel_index", "FresnelRefractiveIndex", 1.33),
        ("reflect_index", "ReflectHDRMult", 1.0),
        ("displace_tangent_space", "VectorDisplacementTS", False),
        ("x", "VDMSwizzleX", "X+"),
        ("y", "VDMSwizzleY", "Y+"),
        ("z", "VDMSwizzleZ", "Z+"),
        ("batch_protect", "BatchProtect", False),
        ("cast_shadows", "CastShadows", True),
        ("receive_shadows", "ReceiveShadows", True),
        ("cull_backfaces", "BackfaceCull", True),
        ("normals_x", "NMSwizzleX", "X+"),
        ("normals_y", "NMSwizzleY", "Y+"),
        ("normals_z", "NMSwizzleZ", "Z+"),
        ("cage_file", "CageFile", ""),
        ("high_override_tangent", "HighpolyNormalsOverrideTangentSpace", True),
        ("transparency", "TransparencyMode", None),
        ("alpha_test", "AlphaTestValue", 127),
        ("matte", "Matte", False),
        ("scale", "Scale", 1.0),
        ("match_uvs", "MatchUVs", False),
        ("offset_u", "UOffset", False),
        ("offset_v", "VOffset", False),
        ("position_offset", "PositionOffset", "0.0000;0.0000;0.0000"),
    ]
    
    def lookup(dict, key, default):
        if key in dict: return dict[key]
        else: return default    
    
    low_opts = [(xml, lookup(kwargs, kw, val)) for kw, xml, val in low_opts ]
    
    return low_opts
    
    
def generation_options(out_filename, **kwargs):
    """ Generates two options dictionaries for generation and colors """
    
    kwargs["out"] = os.path.abspath(out_filename)
    
    """
    List of possible generation options in the form: 
        (keyword_argument, xml_name, default_value)
    """
    gen_opts = [
        ("out", "File", ""),
        ("width", "Width", 512),
        ("height", "Height", 512),
        ("edge_padding", "EdgePadding", 2),
        ("bucket_size", "BucketSize", 64),
        
        ("gen_normals", "GenNormals", False),
        ("aa", "AA", 4),
        ("tangent_space", "TangentSpace", True),
        ("closest_if_fails", "ClosestIfFails", False),
        ("discard_backface_hits", "DiscardRayBackFacesHits", True),
        ("normals_x", "SwizzleX", "X+"),
        ("normals_y", "SwizzleY", "Y+"),
        ("normals_z", "SwizzleZ", "Z+"),
        ("normals_high_texture", "BakeHighpolyBaseTex", False),
        ("normals_high_matid", "BakeHighpolyBaseTextureDrawObjectIDIfNoTexture", False),
        
        ("gen_heights", "GenHeights", False),
        ("heights_tonemap", "HeightTonemap", "Interactive"),
        ("heights_min", "HeightMinVal", -10.0),
        ("heights_max", "HeightMaxVal", 10.0),
        
        ("gen_ao", "GenAO", False),
        ("ao_rays", "AORaysPerSample", 128),
        ("ao_distribution", "AODistribution", "Cosine"),
        ("ao_cone_angle", "AOConeAngle", 162.0),
        ("ao_bias", "AOBias", 0.08),
        ("ao_pure_occlude", "AOAllowPureOccluded", True),
        ("ao_limit_ray_distance", "AOLimitRayDistance", False),
        ("ao_atten_const", "AOAttenConstant", 1.0),
        ("ao_atten_linear", "AOAttenLinear", 0.0),
        ("ao_atten_quadratic", "AOAttenCuadratic", 0.0),
        ("ao_jitter", "AOJitter", False),
        ("ao_ignore_backfaces", "AOIgnoreBackfaceHits", False),
        
        ("gen_bent", "GenBent", False),
        ("bent_rays", "BentRaysPerSample", 128),
        ("bent_cone_angle", "BentConeAngle", 162.0),
        ("bent_bias", "BentBias", 0.08),
        ("bent_tangent_space", "BentTangentSpace", False),
        ("bent_limit_ray_distance", "BentLimitRayDistance", True),
        ("bent_jitter", "BentJitter", False),
        ("bent_distribution", "BentDistribution", "Cosine"),
        ("bent_x", "BentSwizzleX", "X+"),
        ("bent_y", "BentSwizzleY", "Y+"),
        ("bent_z", "BentSwizzleZ", "Z+"),
        
        ("gen_prt", "GenPRT", False),
        ("prt_rays", "PRTRaysPerSample", 128),
        ("prt_cone_angle", "PRTConeAngle", 179.5),
        ("prt_bias", "PRTBias", 0.08),
        ("prt_limit_ray_distance", "PRTLimitRayDistance", True),
        ("prt_jitter", "PRTJitter", False),
        ("prt_normalize", "PRTNormalize", True),
        ("prt_threshold", "PRTThreshold", 0.005),
        
        ("gen_proximity","GenProximity", False),
        ("proximity_rays", "ProximityRaysPerSample", 128),
        ("proximity_cone_angle", "ProximityConeAngle", 80.0),
        ("proximity_limit_ray_distance", "ProximityLimitRayDistance", True),
        
        ("gen_convexity", "GenConvexity", False),
        ("convexity_scale", "ConvexityScale", 1.0),
        
        ("gen_thickness", "GenThickness", False),
        
        ("gen_cavity", "GenCavity", False),
        ("cavity_rays", "CavityRaysPerSample", 128),
        ("cavity_jitter", "CavityJitter", False),
        ("cavity_search_radius", "CavitySearchRadius", 0.5),
        ("cavity_contrast", "CavityContrast", 1.25),
        ("cavity_steps", "CavitySteps", 4),
        
        ("gen_wire", "GenWireRays", False),
        ("render_ray_fails", "RenderRayFails", True),
        ("render_wireframe", "RenderWireframe", True),
        
        ("gen_directions", "GenDirections", False),
        ("directions_tangent_space", "DirectionsTS", False),
        ("directions_x", "DirectionsSwizzleX", "X+"),
        ("directions_y", "DirectionsSwizzleY", "Y+"),
        ("directions_z", "DirectionsSwizzleZ", "Z+"),
        ("directions_tonemap", "DirectionsTonemap", "Interactive"),
        ("directions_min", "DirectionsMinVal", -10.0),
        ("directions_max", "DirectionsMaxVal", 10.0),
        
        ("gen_radiosity_normals", "GenRadiosityNormals", False),
        ("radiosity_normals_rays", "RadiosityNormalsRaysPerSample", 128),
        ("radiosity_normals_distribution", "RadiosityNormalsDistribution", "Cosine"),
        ("radiosity_normals_cone_angle", "RadiosityNormalsConeAngle", 162.0),
        ("radiosity_normals_bias", "RadiosityNormalsBias", 0.08),
        ("radiosity_normals_limit_ray_distance", "RadiosityNormalsLimitRayDistance", False),
        ("radiosity_normals_atten_const", "RadiosityNormalsAttenConstant", 1.0),
        ("radiosity_normals_atten_linear", "RadiosityNormalsAttenLinear", 0.0),
        ("radiosity_normals_atten_quadratic", "RadiosityNormalsAttenCuadratic", 0.0),
        ("radiosity_normals_jitter", "RadiosityNormalsJitter", False),
        ("radiosity_normals_contrast", "RadiosityNormalsContrast", 4.0),
        ("radiosity_normals_encode_ao", "RadiosityNormalsEncodeAO", True),
        ("radiosity_normals_coordsys", "RadiosityNormalsCoordSys", "AlibB"),
        ("radiosity_normals_pure_occlusion", "RadiosityNormalsAllowPureOcclusion", False),
        ("radiosity_normals_high_vcols", "BakeHighpolyVCols", False),
        
        ("gen_curve", "GenCurv", False),
        ("curve_rays", "CurvRaysPerSample", 128),
        ("curve_bias", "CurvBias", 0.0001),
        ("curve_cone_angle", "CurvConeAngle", 178.0),
        ("curve_jitter", "CurvJitter", False),
        ("curve_search_dist", "CurvSearchDistance", 0.5),
        ("curve_tonemap", "CurvTonemap", "2Col"),
        ("curve_distribution", "CurvDistribution", "Cosine"),
        ("curve_algorithm", "CurvAlgorithm", "Average"),
        ("curve_smoothing", "CurvSmoothing", True),
        
        ("gen_derivative_normals", "GenDerivNM", False),
        
        ("gen_translucency", "GenTranslu", False),
        ("translucency_rays", "TransluRaysPerSample", 128),
        ("translucency_distribution", "TransluDistribution", "Cosine"),
        ("translucency_cone_angle", "TransluConeAngle", 162.0),
        ("translucency_bias", "TransluBias", 0.0005),
        ("translucency_distance", "TransluDist", 1.0),
        ("translucency_jitter", "TransluJitter", False),
    ]
    
    """
    List of possible color options in the form: 
        (keyword_argument, xml_name, default_value)
        
    While color options are created in a different set,
    conceptually they are the same as generation options
    """
    color_opts = [
        ("normals_background_color", "NMBackgroundColor",(127, 127, 255)),
        ("high_no_texture_color", "BakeHighpolyBaseTextureNoTexCol", (255, 0, 0)),
        ("high_background_color", "BakeHighpolyBaseTextureBackgroundColor", (0, 0, 0)),
        ("heights_background_color", "HMBackgroundColor", (0, 0, 0)),
        ("ao_occluded_color", "AOOccludedColor", (0, 0, 0)),
        ("ao_unoccluded_color", "AOUnoccludedColor", (255, 255, 255)),
        ("ao_background_color", "AOBackgroundColor", (255, 255, 255)),
        ("bent_background_color", "BentBackgroundColor", (127, 127, 255)),
        ("prt_background_color", "PRTBackgroundColor", (0, 0, 0)),
        ("proximity_background_color", "ProximityBackgroundColor", (255, 255, 255)),
        ("convexity_background_color", "ConvexityBackgroundColor", (255, 255, 255)),
        ("cavity_background_color", "CavityBackgroundColor", (255, 255, 255)),
        ("wireframe_color", "RenderWireframeCol", (255, 255, 255)),
        ("cw_color", "RenderCWCol", (0, 0, 255)),
        ("seam_color", "RenderSeamCol", (0, 255, 0)),
        ("ray_fail_color", "RenderRayFailsCol", (255, 0, 0)),
        ("wireframe_background_color", "RenderWireframeBackgroundColor", (0, 0, 0)),
        ("vdm_background_color", "VDMBackgroundColor", (0, 0, 0)),
        ("radiosity_normals_background_color", "RadNMBackgroundColor", (0, 0, 0)),
        ("high_vcols_background_color", "BakeHighpolyVColsBackgroundCol", (255, 255, 255)),
        ("curve_background_color", "CurvBackgroundColor", (0, 0, 0)),
        ("derivative_normals_background_color", "DerivNMBackgroundColor", (0, 0, 0)),
        ("translucency_background_color", "TransluBackgroundColor", (0, 0, 0)),
    ]
    
    def lookup(dict, key, default):
        if key in dict: return dict[key]
        else: return default
    
    gen_opts = [(xml, lookup(kwargs, kw, val)) for kw, xml, val in gen_opts ]
    color_opts = [(xml, lookup(kwargs, kw, val)) for kw, xml, val in color_opts ]
    
    return gen_opts, color_opts
    
    
def config(high_meshes, low_meshes, opts):
    """ Builds a config file using a list of high mesh options, a list of low mesh options and generation options """
    
    def lowercase_bool(o):
        if o[1] is True: return (o[0], "true")
        elif o[1] is False: return (o[0], "false")
        else: return o
    
    gen_opts, color_opts = opts
    
    gen_opts = map(lowercase_bool, gen_opts)
    color_opts = map(lowercase_bool, color_opts)
    
    conf_string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    conf_string += "<Settings xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" Version=\"%s\">\n" % version
    
    conf_string += "  <HighPolyModel DefaultMeshScale=\"1.000000\">\n"
    for h in high_meshes:
        h = map(lowercase_bool, h)
        conf_string += "    <Mesh %s/>\n" % " ".join(['%s="%s"' % o for o in h])
    conf_string += "  </HighPolyModel>\n"
    
    conf_string += "  <LowPolyModel DefaultMeshScale=\"1.000000\">\n"
    for l in low_meshes:
        l = map(lowercase_bool, l)
        conf_string += "    <Mesh %s/>\n" % " ".join(['%s="%s"' % o for o in l])
    conf_string += "  </LowPolyModel>\n"
    
    conf_string += "  <GenerateMaps %s>\n" % " ".join(['%s="%s"' % o for o in gen_opts])
    
    color_opt_string = "\n    ".join(['<%s R="%i" G="%i" B="%i" />' % (o[0], o[1][0], o[1][1], o[1][2]) for o in color_opts])
    conf_string += "    %s\n" % color_opt_string
    
    conf_string += "  </GenerateMaps>\n"
    conf_string += "</Settings>\n"
    
    return conf_string

