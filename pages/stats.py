from assets.libraries import *
from assets.commons import *
from assets.cards import *
from assets.criteria import *

dash.register_page(__name__, path='/stats')

par_spacer='1rem'
progress_thickness='.8rem'

selector_pregunta = dcc.Dropdown(
    id="selector_pregunta",
    options=[{'label': x, 'value': x} for x in PREGUNTAS_TODAS],
    placeholder='Seleccione la pregunta a analizar',
    value=PREGUNTA_INICIAL
)

selector_iniciativa = dcc.Dropdown(
    id="selector_iniciativa",
    options=[],
    placeholder='',
    value=''
)

selector_criterio_entidad = dcc.Dropdown(
    id="selector_criterio_entidad",
    options=[],
    placeholder='',
    value=''
)

selector_criterio_bucle = dcc.Dropdown(
    id="selector_criterio_bucle",
    options=[],
    placeholder='',
    value=''
)

tarjeta_resumen_2021 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Posición 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_2021',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='st',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

tarjeta_resumen_2023 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Posición 2023: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_2023',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='st_2023',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        dbc.Button(id='btn_actualizar_tablas',children='Actualizar componentes', style={'width':'100%'}),
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

tarjeta_total_2023 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Total IIP 2023: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_total',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='stotal',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

zona_velas = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H3(children='Diagrama de velas: ', className="card-title me-2"),
                html.Br(),
                dcc.Graph(id='candlesticks')
            ]
        ),
    ],
)

zona_de_peligro = dbc.Card(
    [
        dbc.CardBody(children=
            [
                html.H3(children='Zona del peligro: ', className="card-title me-2"),
                html.Br(),
                html.H5(children='Selector de iniciativa: ', className="card-title me-2"),
                selector_iniciativa,
                html.Br(),
                html.H5(children='Selector de criterio entidad: ', className="card-title me-2"),
                selector_criterio_entidad,
                html.Br(),
                html.H5(children='Selector de criterio bucle: ', className="card-title me-2"),
                selector_criterio_bucle,
                html.Br(),
                html.H5(children='Entrada de nota: ', className="card-title me-2"),
                html.Br(),
                dbc.Input(id='entrada_nota', value=1.6, placeholder="Ingrese la nota: ", type="number"),
                html.Br(),
                html.Div(id='empty'),
                html.Div(id='empty_2'),
                dbc.Button(id='btn_enviar_nota',children='Enviar nota a excel', style={'width':'100%'}),
            ]
            ),
    ],
)

zona_de_notas = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H3(children='Zona del notas: ', className="card-title me-2"),
                html.Br(),
                html.Div(id='tabla_criterios'),
            ]
        ),
    ],
)

zona_descarga = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Button("Exportar respuestas 2023", id="btn_download_respuestas_2023", style={'width':'100%'}),
                dcc.Download(id="download_respuestas_2023"),
                html.Br(),
                html.Br(),
                dbc.Button("Exportar resultados 2023", id="btn_download_resultados_2023", style={'width':'100%'}),
                dcc.Download(id="download_resultados_2023"),
                html.Br(),
                html.Br(),
                dbc.Button("Exportar repeats", id="btn_download_repeats", style={'width':'100%'}),
                dcc.Download(id="download_repeats"),
            ]
        ),
    ],
)

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = dbc.Container([

    #FILA 1
    dbc.Row([
        
        dcc.Store(id='pregunta_seleccionada',storage_type='memory'),
        dcc.Store(id='iniciativa_seleccionada',storage_type='memory'),
        dcc.Store(id='criterio_seleccionado_entidad',storage_type='memory'),
        dcc.Store(id='criterio_seleccionado_bucle',storage_type='memory'),
        dcc.Store(id='criterios_disponibles_bucle',storage_type='memory'),
        dcc.Store(id='nota',storage_type='memory'),

        dcc.Store(id='val1',storage_type='memory'),
        dcc.Store(id='val2',storage_type='memory'),
        dcc.Store(id='val3',storage_type='memory'),
        dcc.Store(id='val4',storage_type='memory'),
        dcc.Store(id='val5',storage_type='memory'),
        dcc.Store(id='val6',storage_type='memory'),
        dcc.Store(id='val7',storage_type='memory'),
        dcc.Store(id='val8',storage_type='memory'),

        #Nombre entidad seleccionada
        dbc.Col([
            html.H1(children=[],id='nom_ent',style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=9,
        ),

        #Selector pregunta
        dbc.Col([
            selector_pregunta
            ],
            width=3,
        )
        ],
        justify="between",
        
    ),

    #FILA 2
    dbc.Row([

        #Mision, visión, pregunta, respuesta, criterio, respuesta 2021 y respuesta 2023
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Mision'),
                        html.P(id='mision',children=[])
                    ],                        
                    style={'padding':f'0rem 2rem 0rem 0rem','text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
                dbc.Col([
                    html.Div([
                        html.H3('Vision'),
                        html.P(id='vision',children=[])
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Pregunta'),
                        html.P(id='pregunta',children=[]),
                    ],                        
                    style={'padding':f'0rem 2rem 0rem 0rem','text-justify':'auto','text-align': 'justify'}
                    ),
                ]),

                dbc.Col([
                    html.Div([
                        html.H3('Respuesta 2021'),
                        html.P(id='respuesta_2021',children=[]),

                        html.H5('Nota obtenida en 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                        html.H5(id='nota_obtenida_2021',children=20, className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        html.Br(),
                        html.H5('Nota máxima en 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                        html.H5(id='nota_max_2021',children=20, className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Criterio de evaluación'),
                        html.Div(id='criterio',children=[]),
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3(f'Respuesta 2023'),
                        html.Div(id='respuesta_2023',children='',),
                    ]),
                ]),
            ]),
        ],
        width=9,
        style={'padding':f'0rem 1.5rem 0rem 0rem'}
        ),
            
        #Tarjeta resumen 2021, zona de peligro, zona de descarga
        dbc.Col([
            tarjeta_resumen_2021,
            html.Br(),
            tarjeta_resumen_2023,
            html.Br(),
            tarjeta_total_2023,
            html.Br(),
            zona_de_peligro,
            html.Br(),
            zona_de_notas,
            html.Br(),
            zona_velas,
            html.Br(),
            zona_descarga

        ],
        width=3
        )

    ],
    justify="end",
    ),
])

###############################################################################################################################################################################################################
# CALLBACKS
###############################################################################################################################################################################################################

#Callback guardar pregunta seleccionada
@dash.callback(
    Output('pregunta_seleccionada', 'data'),
    Input('selector_pregunta', 'value')
)
def seleccion_pregunta(value):
    if value != None:
        salida=value
    else:
        salida = preguntas_df[preguntas_df["codigo 2023"] == "p1"]["codigo 2023"].tolist()[0]
    return salida

#Callback guardar iniciativa seleccionada
@dash.callback(
    Output('iniciativa_seleccionada', 'data'),
    Input('selector_iniciativa', 'value')
)
def seleccion_iniciativa(value):
    return value

#Callback guardar criterio entidad seleccionado
@dash.callback(
    Output('criterio_seleccionado_entidad', 'data'),
    Input('selector_criterio_entidad', 'value'),
)
def seleccion_criterio_entidad(entidad):
    return entidad

#Callback enviar criterios bucle
@dash.callback(
    Output('selector_criterio_bucle', 'options'),
    Output('selector_criterio_bucle', 'value'),

    Input('criterio_seleccionado_entidad', 'data'),
    State('pregunta_seleccionada', 'data'),
)
def enviar_criterios_bucle(criterio_seleccionado,pregunta_seleccionada):
    salida_criterios_bucle=[]
    salida_criterios_bucle_seleccionado='N/A'
    unwanted=['l1','l2','l3','l4']
    
    if pregunta_seleccionada=='p1':
        pass
        
    elif pregunta_seleccionada=='p2':
        pass

    elif pregunta_seleccionada=='p3':
        pass
        
    elif pregunta_seleccionada=='p4':
        pass
        
    elif pregunta_seleccionada=='p5':
        pass
        
    elif pregunta_seleccionada=='p6':
        pass
        
    elif pregunta_seleccionada=='p7':
        pass
        
    elif pregunta_seleccionada=='p8':
        pass
        
    elif pregunta_seleccionada=='p9':
        pass
        
    elif pregunta_seleccionada=='p10':
        pass
        
    elif pregunta_seleccionada=='p11':
        pass
        
    elif pregunta_seleccionada=='p12':
        pass
        
    elif pregunta_seleccionada=='p13':
        pass
        
    elif pregunta_seleccionada=='p14':
        pass
        
    elif pregunta_seleccionada=='p15':
        pass
        
    elif pregunta_seleccionada=='p16':
        pass

    elif pregunta_seleccionada=='p17':
        pass
        
    elif pregunta_seleccionada=='p18':
        pass
        
    elif pregunta_seleccionada=='p19':
        pass
        
    elif pregunta_seleccionada=='p20':
        pass
        
    elif pregunta_seleccionada=='p21':
        pass
        
    elif pregunta_seleccionada=='p22':
        pass
        
    elif pregunta_seleccionada=='p23':
        if criterio_seleccionado=='c1':   
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c3':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c4':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    elif pregunta_seleccionada=='p24':
        pass

    elif pregunta_seleccionada=='p25':
        pass
        
    elif pregunta_seleccionada=='p26':
        pass
        
    elif pregunta_seleccionada=='p27':
        pass
        
    elif pregunta_seleccionada=='p28':

        if criterio_seleccionado=='c4':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c5':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    elif pregunta_seleccionada=='p29':
        pass
        
    elif pregunta_seleccionada=='p30':
        pass
        
    elif pregunta_seleccionada=='p31':
        pass
        
    elif pregunta_seleccionada=='p32':
        pass
        
    elif pregunta_seleccionada=='p33':
        pass
        
    elif pregunta_seleccionada=='p34':
        pass
        
    elif pregunta_seleccionada=='p35':
        pass
        
    elif pregunta_seleccionada=='p36':
        pass
        
    elif pregunta_seleccionada=='p37':
        pass
        
    elif pregunta_seleccionada=='p38':
        pass
        
    elif pregunta_seleccionada=='p39':
        pass
    
    return salida_criterios_bucle,salida_criterios_bucle_seleccionado

#Callback guardar criterio bucle seleccionado
@dash.callback(
    Output('criterio_seleccionado_bucle', 'data'),
    Output('criterios_disponibles_bucle', 'data'),
    Input('selector_criterio_bucle', 'value'),
    Input('selector_criterio_bucle', 'options'),
)
def seleccion_criterio_bucle(bucle,opciones_bucle):
    return bucle,opciones_bucle

#Callback para llamar valor de nota
@dash.callback(
    Output('nota', 'data'),
    Input('entrada_nota', 'value'),
)
def llamar_numero(valor):
    return valor

#Callback ver respuestas
@dash.callback(
    Output('pregunta', 'children'),
    Output('criterio', 'children'),
    Output('respuesta_2021', 'children'),
    Output('nota_obtenida_2021', 'children'),
    Output('nota_max_2021', 'children'),
    Output('respuesta_2023', 'children'),
    Output('selector_iniciativa', 'options'),
    Output('selector_iniciativa', 'value'),
    Output('selector_criterio_entidad', 'options'),
    Output('selector_criterio_entidad', 'value'),

    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
)
def visualizacion_respuestas(entidad_seleccionada,pregunta_seleccionada):
  
    def test_empty_pregunta(entidad_seleccionada,pregunta_seleccionada):
        #pregunta textual
        try:
            pregunta = preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['pregunta 2023']
            salida_pregunta=pregunta
            out_pre='Success'
        except Exception as e_pre:
            pregunta = 'N/A'
            salida_pregunta=pregunta
            out_pre=f"|||PREGUNTA||| Couldn't load pregunta due to {e_pre}"
            print(out_pre)

        return salida_pregunta,out_pre
    
    def test_empty_respuesta_2021(entidad_seleccionada,pregunta_seleccionada):
        #respuesta 2021
        try:
            respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada]
            if respuesta_2021.empty ==False:
                salida_respuesta_2021=respuesta_2021
            else:
                salida_respuesta_2021 = 'N/A'
            out_2021='Success'
        except Exception as e_res_2021:
            salida_respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p1']
            out_2021=f"|||RESPUESTA 2021||| Couldn't load respuesta 2021 due to {e_res_2021}"
            print(out_2021)
        
        return salida_respuesta_2021,out_2021
    
    def test_empty_respuesta_2023(entidad_seleccionada,pregunta_seleccionada):
        #Respuesta 2023
        try:
            respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada]
            if respuesta_2023.empty ==False:
                salida_respuesta_2023=respuesta_2023
            else:
                salida_respuesta_2023 = 'N/A'
            out_2023='Success'
        except Exception as e_res_2023:
            salida_respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p1']
            out_2023=f"|||RESPUESTA 2023||| Couldn't load respuesta 2023 due to {e_res_2023}"
            print(out_2023)

        return salida_respuesta_2023,out_2023

    pregunta,error_pregunta=test_empty_pregunta(entidad_seleccionada,pregunta_seleccionada)
    respuesta_2021,error_2021=test_empty_respuesta_2021(entidad_seleccionada,pregunta_seleccionada)
    respuesta_2023,error_2023=test_empty_respuesta_2023(entidad_seleccionada,pregunta_seleccionada)

    estilo={'display':'flex','flex-wrap': 'wrap','justify-content':'space-between'}
    indices_carousel=[0]
    salida_criterio=indices_carousel

    if pregunta_seleccionada=='p1':

        indices_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_1()
        
    elif pregunta_seleccionada=='p2':

        indices_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_2()

    elif pregunta_seleccionada=='p3':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis=0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent=0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_3()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p4':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis = 0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent=0

        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_4()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p5':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis =0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent =0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_5()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p6':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis = 0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_cos*100/rel_enti_pre
        except:
            res_ent = 0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_6()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p7':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis = 0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_7()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p8':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_8()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p9':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p8'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada]['p8']
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_9()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p10':
        
        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_10()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p11':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])

        salida_criterio=criterio_11()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p12':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p11'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada]['p11']
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_12()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p13':

        indices_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        costo_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cos']
        soportes_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p13(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        cos_car=list(costo_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_13()
        
    elif pregunta_seleccionada=='p14':

        indices_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada])[0]
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:

                try:
                    act_4_otr = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]                
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_14()
        
    elif pregunta_seleccionada=='p15':

        indices_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_15()
        
    elif pregunta_seleccionada=='p16':

        indices_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rom']
        act_1_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_16()
        
    elif pregunta_seleccionada=='p17':
        
        indices_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_can']
        usuarios_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_17()
        
    elif pregunta_seleccionada=='p18':

        indices_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act']
        usuarios_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p17'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=["N/A"]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())

        salida_criterio=criterio_18()
        
    elif pregunta_seleccionada=='p19':

        indices_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_19()
        
    elif pregunta_seleccionada=='p20':

        indices_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_20()
        
    elif pregunta_seleccionada=='p21':

        indices_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_can']
        usuarios_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_21()
        
    elif pregunta_seleccionada=='p22':

        indices_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act']
        usuarios_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p21'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad='N/A'
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_22()
        
    elif pregunta_seleccionada=='p23':

        indices_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']
        usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_1']
        usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_2']
        usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_3']
        prototipado = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_pro']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    vali_usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_1']
                    vali_usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_2']
                    vali_usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_3']
                except:
                    vali_usr_1_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_2_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_3_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p23(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        us1_car=list(usr_1_carousel)[i],
                        us2_car=list(usr_2_carousel)[i],
                        us3_car=list(usr_3_carousel)[i],
                        pro_car=list(prototipado)[i],
                        va1_car=list(vali_usr_1_carousel)[i],
                        va2_car=list(vali_usr_2_carousel)[i],
                        va3_car=list(vali_usr_3_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_23()
        
    elif pregunta_seleccionada=='p24':

        p24_1_indices_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_1_codigos_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_nom']
        p24_1_descripciones_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_des']
        p24_1_impartio_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_imp']
        p24_1_asistentes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_asi']
        p24_1_soportes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_sop']

        p24_2_indices_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_2_codigos_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_nom']
        p24_2_descripciones_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_des']
        p24_2_impartio_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_imp']
        p24_2_asistentes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_asi']
        p24_2_soportes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_sop']

        p24_3_indices_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_3_codigos_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_nom']
        p24_3_descripciones_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_des']
        p24_3_impartio_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_imp']
        p24_3_asistentes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_asi']
        p24_3_soportes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_sop']

        p24_4_indices_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_4_codigos_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_nom']
        p24_4_descripciones_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_des']
        p24_4_impartio_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_imp']
        p24_4_asistentes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_asi']
        p24_4_soportes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_sop']

        p24_5_indices_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_5_codigos_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_nom']
        p24_5_descripciones_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_des']
        p24_5_impartio_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_imp']
        p24_5_asistentes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_asi']
        p24_5_soportes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':

            if p24_1_indices_carousel.empty == False:
                cards1=[]
                for i in range(len(p24_1_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_1_indices_carousel)[i],
                        nom_car=list(p24_1_codigos_carousel)[i],
                        des_car=list(p24_1_descripciones_carousel)[i],
                        imp_car=list(p24_1_impartio_carousel)[i],
                        asi_car=list(p24_1_asistentes_carousel)[i],
                        sop_car=list(p24_1_soportes_carousel)[i])
                    cards1.append(card)
            else:
                cards1=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if p24_2_indices_carousel.empty == False:
                cards2=[]
                for i in range(len(p24_2_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_2_indices_carousel)[i],
                        nom_car=list(p24_2_codigos_carousel)[i],
                        des_car=list(p24_2_descripciones_carousel)[i],
                        imp_car=list(p24_2_impartio_carousel)[i],
                        asi_car=list(p24_2_asistentes_carousel)[i],
                        sop_car=list(p24_2_soportes_carousel)[i])
                    cards2.append(card)
            else:
                cards2=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if p24_3_indices_carousel.empty == False:
                cards3=[]
                for i in range(len(p24_3_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_3_indices_carousel)[i],
                        nom_car=list(p24_3_codigos_carousel)[i],
                        des_car=list(p24_3_descripciones_carousel)[i],
                        imp_car=list(p24_3_impartio_carousel)[i],
                        asi_car=list(p24_3_asistentes_carousel)[i],
                        sop_car=list(p24_3_soportes_carousel)[i])
                    cards3.append(card)
            else:
                cards3=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if p24_4_indices_carousel.empty == False:
                cards4=[]
                for i in range(len(p24_4_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_4_indices_carousel)[i],
                        nom_car=list(p24_4_codigos_carousel)[i],
                        des_car=list(p24_4_descripciones_carousel)[i],
                        imp_car=list(p24_4_impartio_carousel)[i],
                        asi_car=list(p24_4_asistentes_carousel)[i],
                        sop_car=list(p24_4_soportes_carousel)[i])
                    cards4.append(card)
            else:
                cards4=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if p24_5_indices_carousel.empty == False:
                cards5=[]
                for i in range(len(p24_5_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_5_indices_carousel)[i],
                        nom_car=list(p24_5_codigos_carousel)[i],
                        des_car=list(p24_5_descripciones_carousel)[i],
                        imp_car=list(p24_5_impartio_carousel)[i],
                        asi_car=list(p24_5_asistentes_carousel)[i],
                        sop_car=list(p24_5_soportes_carousel)[i])
                    cards5.append(card)
            else:
                cards5=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            salida_respuesta_2023 = html.Div([
                    html.H5('Eventos Auspiciados y/o financiados directamente por esa entidad'),
                    html.Div(children=cards1,style=estilo),
                    html.H5('Eventos Auspiciados y/o financiados directamente por otras entidades'),
                    html.Div(children=cards2,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por esa entidad'),
                    html.Div(children=cards3,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por otras entidades'),
                    html.Div(children=cards4,style=estilo),
                    html.H5('Otras actividades de esa entidad'),
                    html.Div(children=cards5,style=estilo),
                ])
            
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_24()
        
    elif pregunta_seleccionada=='p25':

        indices_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        recomendacion_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rec']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_25()
        
    elif pregunta_seleccionada=='p26':

        indices_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        recomendacion_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rec']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_26()
        
    elif pregunta_seleccionada=='p27':

        indices_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        tematica_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des_001']
        tamano_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_c']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p27(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        tem_car=list(tematica_carousel)[i],
                        tam_car=list(tamano_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_27()
        
    elif pregunta_seleccionada=='p28':

        indices_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'nom_inno']
        implementado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_imp']
        validado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val']
        metodologia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'meto']
        beneficia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_ben']
        ahorro_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_aho']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(beneficia_carousel)[0]=='Si':
                    beneficiados_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'beneficiados']
                else:
                    beneficiados_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                
                if list(ahorro_carousel)[0]=='Si':
                    ahorrado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'recursos_ahorrados']
                else:
                    ahorrado_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p28(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        imp_car=list(implementado_carousel)[i],
                        val_car=list(validado_carousel)[i],
                        met_car=list(metodologia_carousel)[i],
                        ben_car=list(beneficia_carousel)[i],
                        aho_car=list(ahorro_carousel)[i],
                        b1_car=list(beneficiados_carousel)[i],
                        a1_car=list(ahorrado_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_28()
        
    elif pregunta_seleccionada=='p29':

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        total_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        formados_2021_dis = respuestas_2023_df[f'p29_val_1'].median()
        formados_2022_dis = respuestas_2023_df[f'p29_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p29_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p29_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        try:
            res_dis = rel_dist_for*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_for*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_29()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p30':

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        total_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        formados_2021_dis = respuestas_2023_df[f'p30_val_1'].median()
        formados_2022_dis = respuestas_2023_df[f'p30_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p30_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p30_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        try:
            res_dis = rel_dist_for*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_for*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_30()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p31':

        indices_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_31()
        
    elif pregunta_seleccionada=='p32':

        indices_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_32()
        
    elif pregunta_seleccionada=='p33':

        indices_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_33()
        
    elif pregunta_seleccionada=='p34':

        indices_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_34()
        
    elif pregunta_seleccionada=='p35':

        indices_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_35()
        
    elif pregunta_seleccionada=='p36':

        indices_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_36()
        
    elif pregunta_seleccionada=='p37':

        indices_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_37()
        
    elif pregunta_seleccionada=='p38':

        indices_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_38()
        
    elif pregunta_seleccionada=='p39':

        indices_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p39(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_39()
        
    else:
        salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Caso no definido',
                    color="danger",
                    dismissable=True,
                    is_open=True)])


    if pregunta_seleccionada == 'p3':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p4':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p5':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p6':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p7':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p8':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'
    
    elif pregunta_seleccionada == 'p9':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p10':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p11':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p12':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p24':
        salida_iniciativas=list(itertools.chain(p24_1_indices_carousel,p24_2_indices_carousel,p24_3_indices_carousel,p24_4_indices_carousel))

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p29':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p30':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    else:
        salida_iniciativas=list(indices_carousel)
        
        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    return pregunta,salida_criterio,salida_respuesta_2021,salida_nota_2021,salida_max_2021,salida_respuesta_2023,salida_iniciativas,salida_iniciativa_seleccionada,salida_criterios_entidad,salida_criterios_entidad_seleccionado

#Callback calificar iniciativa seleccionada
@dash.callback(
    Output('val1', 'data'),
    Output('val2', 'data'),
    Output('val3', 'data'),
    Output('val4', 'data'),
    Output('val5', 'data'),
    Output('val6', 'data'),
    Output('val7', 'data'),
    Output('val8', 'data'),

    Input('btn_enviar_nota', 'n_clicks'),

    State('entidad_seleccionada', 'data'),
    State('pregunta_seleccionada', 'data'),
    State('iniciativa_seleccionada', 'data'),
    State('criterio_seleccionado_entidad', 'data'),
    State('criterio_seleccionado_bucle', 'data'),
    State('criterios_disponibles_bucle', 'data'),
    State('nota', 'data'),
    prevent_initial_call=True,
)
def calificacion_iniciativa(clicks,entidad_seleccionada,pregunta_seleccionada,iniciativa_seleccionada,criterio_seleccionado,criterio_seleccionado_bucle,criterios_disponibles_bucle,nota):

    vals={
        'val1':'N/A',
        'val2':'N/A',
        'val3':'N/A',
        'val4':'N/A',
        'val5':'N/A',
        'val6':'N/A',
        'val7':'N/A',
        'val8':'N/A',
    }

    if clicks is not None:
        if pregunta_seleccionada=='p1':
            pass

        elif pregunta_seleccionada=='p2':
            p2_df=pd.read_excel(UBI_AR['p2'])
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
                
            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            elif criterio_seleccionado=='c3':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO
                p2_df.loc[p2_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
                
                nota_entidad = round(p2_df.loc[p2_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota_entidad

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'].to_string(index=False)
            vals['val4']=p2_df.loc[p2_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c3'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p2_df.to_excel(UBI_AR['p2'],index=False)
            respuestas_2023_df.to_excel(UBI_AR['respuestas_2023'],index=False)
            resultados_2023_df.to_excel(UBI_AR['resultados_2023'],index=False)

        elif pregunta_seleccionada=='p3':
            pass

        elif pregunta_seleccionada=='p4':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])
            
            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p5':
            pass

        elif pregunta_seleccionada=='p6':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])
            
            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p7':
            pass

        elif pregunta_seleccionada=='p8':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p9':
            pass

        elif pregunta_seleccionada=='p10':
            pass

        elif pregunta_seleccionada=='p11':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p12':
            pass

        elif pregunta_seleccionada=='p13':
            p13_df=pd.read_excel('./files/separadas/repeat_p13.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])
            
            if criterio_seleccionado=='c1':   
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p13_df.loc[p13_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p13_df.loc[p13_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p13_df.loc[p13_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p13_df.to_excel(f'./files/separadas/repeat_p13.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p14':
            p14_df=pd.read_excel('./files/separadas/repeat_p14.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p14_df.loc[p14_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p14_df.loc[p14_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p14_df.loc[p14_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p14_df.to_excel(f'./files/separadas/repeat_p14.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p15':
            p15_df=pd.read_excel('./files/separadas/repeat_p15.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p15_df.loc[p15_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
                
                nota_entidad = round(p15_df.loc[p15_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p15_df.loc[p15_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p15_df.to_excel(f'./files/separadas/repeat_p15.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p16':
            p16_df=pd.read_excel('./files/separadas/repeat_p16.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p16_df.loc[p16_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
        
                nota_entidad = round(p16_df.loc[p16_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad                

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p16_df.loc[p16_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p16_df.to_excel(f'./files/separadas/repeat_p16.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p17':
            p17_df=pd.read_excel('./files/separadas/repeat_p17.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p17_df.loc[p17_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
        
                nota_entidad = round(p17_df.loc[p17_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad                

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p17_df.loc[p17_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p17_df.to_excel(f'./files/separadas/repeat_p17.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p18':
            p18_df=pd.read_excel('./files/separadas/repeat_p18.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p18_df.loc[p18_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p18_df.loc[p18_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p18_df.loc[p18_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p18_df.to_excel(f'./files/separadas/repeat_p18.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p19':
            p19_df=pd.read_excel('./files/separadas/repeat_p19.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p19_df.loc[p19_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p19_df.loc[p19_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p19_df.loc[p19_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p19_df.to_excel(f'./files/separadas/repeat_p19.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p20':
            p20_df=pd.read_excel('./files/separadas/repeat_p20.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p20_df.loc[p20_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p20_df.loc[p20_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p20_df.loc[p20_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p20_df.to_excel(f'./files/separadas/repeat_p20.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p21':
            p21_df=pd.read_excel('./files/separadas/repeat_p21.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p21_df.loc[p21_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p21_df.loc[p21_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p21_df.loc[p21_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p21_df.to_excel(f'./files/separadas/repeat_p21.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p22':
            p22_df=pd.read_excel('./files/separadas/repeat_p22.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p22_df.loc[p22_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p22_df.loc[p22_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p22_df.loc[p22_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p22_df.to_excel(f'./files/separadas/repeat_p22.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p23':
            p23_df=pd.read_excel('./files/separadas/repeat_p23.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c1']=nota

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad
            
            elif criterio_seleccionado=='c2':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c2']=nota

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c2'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad

            elif criterio_seleccionado=='c3':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c3']=nota

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c3'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota_entidad

            elif criterio_seleccionado=='c4':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c4']=nota

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c4'].mean(),4)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c1'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val4']=p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c2'].to_string(index=False)
            vals['val5']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'].to_string(index=False)
            vals['val6']=p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c3'].to_string(index=False)
            vals['val7']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'].to_string(index=False)
            vals['val8']=p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c4'].to_string(index=False)

            p23_df['nota_iniciativa']=p23_df['c1']+p23_df['c2']+p23_df['c3']+p23_df['c4']

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c4'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p24':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

            elif criterio_seleccionado=='c3':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota

            elif criterio_seleccionado=='c4':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'].to_string(index=False)
            vals['val4']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'].to_string(index=False)
            
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c4'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p25':
            p25_df=pd.read_excel('./files/separadas/repeat_p25.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p25_df.loc[p25_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p25_df.loc[p25_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p25_df.loc[p25_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p25_df.to_excel(f'./files/separadas/repeat_p25.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p26':
            p26_df=pd.read_excel('./files/separadas/repeat_p26.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p26_df.loc[p26_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p26_df.loc[p26_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p26_df.loc[p26_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p26_df.to_excel(f'./files/separadas/repeat_p26.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p27':
            p27_df=pd.read_excel('./files/separadas/repeat_p27.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p27_df.loc[p27_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p27_df.loc[p27_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=p27_df.loc[p27_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p27_df.to_excel(f'./files/separadas/repeat_p27.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p28':
            p28_df=pd.read_excel('./files/separadas/repeat_p28.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

            elif criterio_seleccionado=='c3':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota

            elif criterio_seleccionado=='c4':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p28_df.loc[p28_df['_index']==iniciativa_seleccionada, 'c4']=nota

                nota_entidad = round(p28_df.loc[p28_df['_submission__uuid']==entidad_seleccionada]['c4'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota_entidad

            elif criterio_seleccionado=='c5':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p28_df.loc[p28_df['_index']==iniciativa_seleccionada, 'c5']=nota

                nota_entidad = round(p28_df.loc[p28_df['_submission__uuid']==entidad_seleccionada]['c5'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'].to_string(index=False)
            vals['val4']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'].to_string(index=False)
            vals['val5']=p28_df.loc[p28_df['_index']==iniciativa_seleccionada, 'c4'].to_string(index=False)
            vals['val6']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'].to_string(index=False)
            vals['val7']=p28_df.loc[p28_df['_index']==iniciativa_seleccionada, 'c5'].to_string(index=False)

            p28_df['nota_iniciativa']=p28_df['c4']+p28_df['c5']

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c5'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p28_df.to_excel(f'./files/separadas/repeat_p28.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p29':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p30':
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
                
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p31':
            pass

        elif pregunta_seleccionada=='p32':
            p32_df=pd.read_excel('./files/separadas/repeat_p32.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p32_df.loc[p32_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p32_df.loc[p32_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p32_df.loc[p32_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p32_df.to_excel(f'./files/separadas/repeat_p32.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p33':
            p33_df=pd.read_excel('./files/separadas/repeat_p33.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':   
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p33_df.loc[p33_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p33_df.loc[p33_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p33_df.loc[p33_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p33_df.to_excel(f'./files/separadas/repeat_p33.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p34':
            p34_df=pd.read_excel('./files/separadas/repeat_p34.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p34_df.loc[p34_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p34_df.loc[p34_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p34_df.loc[p34_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p34_df.to_excel(f'./files/separadas/repeat_p34.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p35':
            p35_df=pd.read_excel('./files/separadas/repeat_p35.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':   
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p35_df.loc[p35_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p35_df.loc[p35_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p35_df.loc[p35_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p35_df.to_excel(f'./files/separadas/repeat_p35.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p36':
            p36_df=pd.read_excel('./files/separadas/repeat_p36.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p36_df.loc[p36_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p36_df.loc[p36_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p36_df.loc[p36_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p36_df.to_excel(f'./files/separadas/repeat_p36.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p37':
            p37_df=pd.read_excel('./files/separadas/repeat_p37.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':   
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p37_df.loc[p37_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
                
                nota_entidad = round(p37_df.loc[p37_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p37_df.loc[p37_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p37_df.to_excel(f'./files/separadas/repeat_p37.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p38':
            p38_df=pd.read_excel('./files/separadas/repeat_p38.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p38_df.loc[p38_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

                nota_entidad = round(p38_df.loc[p38_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p38_df.loc[p38_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p38_df.to_excel(f'./files/separadas/repeat_p38.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        elif pregunta_seleccionada=='p39':
            p39_df=pd.read_excel('./files/separadas/repeat_p39.xlsx')
            resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])
            respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

            if criterio_seleccionado=='c1':  
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p39_df.loc[p39_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
                
                nota_entidad = round(p39_df.loc[p39_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
            
            else:
                pass

            vals['val1']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].to_string(index=False)
            vals['val2']=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'].to_string(index=False)
            vals['val3']=p39_df.loc[p39_df['_index']==iniciativa_seleccionada, 'nota_iniciativa'].to_string(index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            p39_df.to_excel(f'./files/separadas/repeat_p39.xlsx',index=False)
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        else:
            pass

    v1=vals['val1']
    v2=vals['val2']
    v3=vals['val3']
    v4=vals['val4']
    v5=vals['val5']
    v6=vals['val6']
    v7=vals['val7']
    v8=vals['val8']
    print(v1,v2,v3,v4,v5,v6,v7,v8)
    return v1,v2,v3,v4,v5,v6,v7,v8

#Callback actualizar valores por componente
@dash.callback(
    Output('empty','children'),

    Input('btn_actualizar_tablas','n_clicks'),
    Input('entidad_seleccionada', 'data'),
)
def actualizar_totales(click,entidad_seleccionada):

    resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')

    resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p1':'p13'].sum().sum(),2)
    resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c2'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p14':'p27'].sum().sum(),2)
    resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c3'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p28':'p30'].sum().sum(),2)
    resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c4'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p31':'p39'].sum().sum(),2)
    resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'total'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1':'res_c4'].sum().sum(),2)
    
    resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

#Callback cargar tabla
@dash.callback(
    Output('tabla_criterios', 'children'),

    Input('btn_enviar_nota', 'n_clicks'),
    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
    Input('iniciativa_seleccionada', 'data'),
    Input('criterio_seleccionado_entidad', 'data'),
    Input('criterio_seleccionado_bucle', 'data'),
    Input('criterios_disponibles_bucle', 'data'),
    Input('nota', 'data'),
    
    State('val1', 'data'),
    State('val2', 'data'),
    State('val3', 'data'),
    State('val4', 'data'),
    State('val5', 'data'),
    State('val6', 'data'),
    State('val7', 'data'),
    State('val8', 'data'),
)
def cargar_tabla(enviar_nota,entidad_seleccionada,pregunta_seleccionada,iniciativa_seleccionada,criterio_seleccionado_entidad,criterio_seleccionado_bucle,criterios_disponibles_bucle,nota,val1,val2,val3,val4,val5,val6,val7,val8):

    vals={
        'val1':val1,
        'val2':val2,
        'val3':val3,
        'val4':val4,
        'val5':val5,
        'val6':val6,
        'val7':val7,
        'val8':val8,
    }

    if pregunta_seleccionada=='p1':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p2':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val2'],rowSpan=2),
                        html.Td(vals['val3']),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val4']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p3':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p4':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p5':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p6':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p7':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p8':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios
        
    elif pregunta_seleccionada=='p9':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p10':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p11':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p12':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p13':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val2']),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val3']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p14':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p15':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p16':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p17':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p18':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p19':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p20':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p21':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p22':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p23':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3']),
                        html.Td(vals['val5']),
                        html.Td(vals['val7']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                        html.Td(vals['val4']),
                        html.Td(vals['val6']),
                        html.Td(vals['val8']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p24':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val2']),
                        html.Td(vals['val3']),
                        html.Td(vals['val4']),
                        
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p25':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p26':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        html.Td(vals['val3'],rowSpan=2),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p27':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p28':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4'),
                        html.Th(f'c5'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val2'],rowSpan=2),
                        html.Td(vals['val3'],rowSpan=2),
                        html.Td(vals['val4']),
                        html.Td(vals['val6']),
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val5']),
                        html.Td(vals['val7']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),


        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p29':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p30':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1']),
                        
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p31':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p32':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p33':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p34':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p35':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p36':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p37':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p38':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    elif pregunta_seleccionada=='p39':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(vals['val1'],rowSpan=2),
                        html.Td(vals['val3']),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(vals['val2']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
        return tabla_criterios

    else:
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

#Callback nombre, misión y visión
@dash.callback(
    Output('nom_ent', 'children'),
    Output('mision', 'children'),
    Output('vision', 'children'),
    Input('entidad_seleccionada', 'data')
)
def mision_vision_entidad_f(value):

    nom_ent= respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['entidad']
    
    mis = respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['mision']
    vis = respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['vision']

    if mis.empty ==False:
        mis_ent=mis
    else:
        mis_ent = 'N/A'

    if vis.empty ==False:
        vis_ent=vis
    else:
        vis_ent = 'N/A'

    return nom_ent,mis_ent,vis_ent

#Callback resumen 2021 lateral
@dash.callback(
    Output('posicion_2021', 'children'),
    Output('st', 'label'),
    Output('sc1', 'label'),
    Output('sc2', 'label'),
    Output('sc3', 'label'),
    Output('sc4', 'label'),
    Output('st', 'value'),
    Output('sc1', 'value'),
    Output('sc2', 'value'),
    Output('sc3', 'value'),
    Output('sc4', 'value'),
    Input('entidad_seleccionada', 'data')
)
def tabla_resumen_2021(entidad):
    
    pos = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['pos']
    if pos.empty == False:
        pos_2021 = pos
    else:
        pos_2021 = 'N/A'

    total = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['total'].round(2)
    if total.empty == False:
        res_total  = total
        st = total
    else:
        res_total = 'N/A'
        st = 0

    c1 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c1'].round(2)
    if c1.empty == False:
        res_c1 = c1
        sc1 = c1
    else:
        res_c1 = 'N/A'
        sc1 = 0

    c2 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c2'].round(2)
    if c2.empty == False:
        res_c2 = c2
        sc2 = c2
    else:
        res_c2 = 'N/A'
        sc2 = 0

    c3 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c3'].round(2)
    if c3.empty == False:
        res_c3 = c3
        sc3 = c3
    else:
        res_c3 = 'N/A'
        sc3 = 0

    c4 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c4'].round(2)
    if c4.empty == False:
        res_c4 = c4
        sc4 = c4
    else:
        res_c4 = 'N/A'
        sc4 = 0

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback resumen 2023 lateral
@dash.callback(
    Output('posicion_2023', 'children'),
    Output('st_2023', 'label'),
    Output('sc1_2023', 'label'),
    Output('sc2_2023', 'label'),
    Output('sc3_2023', 'label'),
    Output('sc4_2023', 'label'),
    Output('st_2023', 'value'),
    Output('sc1_2023', 'value'),
    Output('sc2_2023', 'value'),
    Output('sc3_2023', 'value'),
    Output('sc4_2023', 'value'),
    Input('entidad_seleccionada', 'data'),
)
def tabla_resumen_2023(entidad_seleccionada):
    resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')

    total = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'total'],2)
    c1 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1']*100/25,2)
    c2 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c2']*100/35,2)
    c3 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c3']*100/25,2)
    c4 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c4']*100/15,2)

    pos_2021 = total

    res_total = total
    st = total

    res_c1 = c1
    sc1 = c1

    res_c2 = c2
    sc2 = c2

    res_c3 = c3
    sc3 = c3

    res_c4 = c4
    sc4 = c4

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback resumen iip lateral
@dash.callback(
    Output('posicion_total', 'children'),
    Output('stotal', 'label'),
    Output('sc1total', 'label'),
    Output('sc2total', 'label'),
    Output('sc3total', 'label'),
    Output('sc4total', 'label'),
    Output('stotal', 'value'),
    Output('sc1total', 'value'),
    Output('sc2total', 'value'),
    Output('sc3total', 'value'),
    Output('sc4total', 'value'),
    Input('entidad_seleccionada', 'data'),
)
def tabla_resumen_total(entidad_seleccionada):
    resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
    
    total = round(resultados_2023_df.loc[:,'total'].mean(),2)
    c1 = round(resultados_2023_df.loc[:,'res_c1'].mean()*100/25,2)
    c2 = round(resultados_2023_df.loc[:,'res_c2'].mean()*100/35,2)
    c3 = round(resultados_2023_df.loc[:,'res_c3'].mean()*100/25,2)
    c4 = round(resultados_2023_df.loc[:,'res_c4'].mean()*100/15,2)

    pos_2021 = total

    res_total = total
    st = total

    res_c1 = c1
    sc1 = c1

    res_c2 = c2
    sc2 = c2

    res_c3 = c3
    sc3 = c3

    res_c4 = c4
    sc4 = c4

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback velas
@dash.callback(
    Output('candlesticks', 'figure'),
    Input('pregunta_seleccionada', 'data'),
)
def diagrama_velas(pregunta_seleccionada):
    
    x_axis = ['2021','2023']
    outliers_top = []
    mean_top = []
    mean_bottom = []
    outliers_bottom = []

    try:
        outliers_top_2021 = resultados_2021_df[pregunta_seleccionada].max()
        mean_top_2021 = resultados_2021_df[pregunta_seleccionada].median() + resultados_2021_df[pregunta_seleccionada].std()
        mean_bottom_2021 = resultados_2021_df[pregunta_seleccionada].median() - resultados_2021_df[pregunta_seleccionada].std()
        outliers_bottom_2021 = resultados_2021_df[pregunta_seleccionada].min()
    except:
        outliers_top_2021 = 0
        mean_top_2021 = 0
        mean_bottom_2021 = 0
        outliers_bottom_2021 = 0
    
    #"""
    
    if pregunta_seleccionada=='p1':

        outliers_top_2023 = p1_df['nota_iniciativa'].max()
        mean_top_2023 = p1_df['nota_iniciativa'].median() + p1_df['nota_iniciativa'].std()
        mean_bottom_2023 = p1_df['nota_iniciativa'].median() - p1_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p1_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p2':

        outliers_top_2023 = p2_df['nota_iniciativa'].max()
        mean_top_2023 = p2_df['nota_iniciativa'].median() + p2_df['nota_iniciativa'].std()
        mean_bottom_2023 = p2_df['nota_iniciativa'].median() - p2_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p2_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p3':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p4':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p5':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p6':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p7':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p8':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p9':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p10':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p11':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p12':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p13':

        outliers_top_2023 = p13_df['nota_iniciativa'].max()
        mean_top_2023 = p13_df['nota_iniciativa'].median() + p13_df['nota_iniciativa'].std()
        mean_bottom_2023 = p13_df['nota_iniciativa'].median() - p13_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p13_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p14':

        outliers_top_2023 = p14_df['nota_iniciativa'].max()
        mean_top_2023 = p14_df['nota_iniciativa'].median() + p14_df['nota_iniciativa'].std()
        mean_bottom_2023 = p14_df['nota_iniciativa'].median() - p14_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p14_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p15':

        outliers_top_2023 = p15_df['nota_iniciativa'].max()
        mean_top_2023 = p15_df['nota_iniciativa'].median() + p15_df['nota_iniciativa'].std()
        mean_bottom_2023 = p15_df['nota_iniciativa'].median() - p15_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p15_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p16':

        outliers_top_2023 = p16_df['nota_iniciativa'].max()
        mean_top_2023 = p16_df['nota_iniciativa'].median() + p16_df['nota_iniciativa'].std()
        mean_bottom_2023 = p16_df['nota_iniciativa'].median() - p16_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p16_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p17':

        outliers_top_2023 = p17_df['nota_iniciativa'].max()
        mean_top_2023 = p17_df['nota_iniciativa'].median() + p17_df['nota_iniciativa'].std()
        mean_bottom_2023 = p17_df['nota_iniciativa'].median() - p17_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p17_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p18':

        outliers_top_2023 = p18_df['nota_iniciativa'].max()
        mean_top_2023 = p18_df['nota_iniciativa'].median() + p18_df['nota_iniciativa'].std()
        mean_bottom_2023 = p18_df['nota_iniciativa'].median() - p18_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p18_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p19':

        outliers_top_2023 = p19_df['nota_iniciativa'].max()
        mean_top_2023 = p19_df['nota_iniciativa'].median() + p19_df['nota_iniciativa'].std()
        mean_bottom_2023 = p19_df['nota_iniciativa'].median() - p19_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p19_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p20':

        outliers_top_2023 = p20_df['nota_iniciativa'].max()
        mean_top_2023 = p20_df['nota_iniciativa'].median() + p20_df['nota_iniciativa'].std()
        mean_bottom_2023 = p20_df['nota_iniciativa'].median() - p20_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p20_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p21':

        outliers_top_2023 = p21_df['nota_iniciativa'].max()
        mean_top_2023 = p21_df['nota_iniciativa'].median() + p21_df['nota_iniciativa'].std()
        mean_bottom_2023 = p21_df['nota_iniciativa'].median() - p21_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p21_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p22':

        outliers_top_2023 = p22_df['nota_iniciativa'].max()
        mean_top_2023 = p22_df['nota_iniciativa'].median() + p22_df['nota_iniciativa'].std()
        mean_bottom_2023 = p22_df['nota_iniciativa'].median() - p22_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p22_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p23':

        outliers_top_2023 = p23_df['nota_iniciativa'].max()
        mean_top_2023 = p23_df['nota_iniciativa'].median() + p23_df['nota_iniciativa'].std()
        mean_bottom_2023 = p23_df['nota_iniciativa'].median() - p23_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p23_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p24':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p25':

        outliers_top_2023 = p25_df['nota_iniciativa'].max()
        mean_top_2023 = p25_df['nota_iniciativa'].median() + p25_df['nota_iniciativa'].std()
        mean_bottom_2023 = p25_df['nota_iniciativa'].median() - p25_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p25_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p26':

        outliers_top_2023 = p26_df['nota_iniciativa'].max()
        mean_top_2023 = p26_df['nota_iniciativa'].median() + p26_df['nota_iniciativa'].std()
        mean_bottom_2023 = p26_df['nota_iniciativa'].median() - p26_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p26_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p27':

        outliers_top_2023 = p27_df['nota_iniciativa'].max()
        mean_top_2023 = p27_df['nota_iniciativa'].median() + p27_df['nota_iniciativa'].std()
        mean_bottom_2023 = p27_df['nota_iniciativa'].median() - p27_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p27_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p28':

        outliers_top_2023 = p28_df['nota_iniciativa'].max()
        mean_top_2023 = p28_df['nota_iniciativa'].median() + p28_df['nota_iniciativa'].std()
        mean_bottom_2023 = p28_df['nota_iniciativa'].median() - p28_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p28_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p29':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p30':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p31':

        outliers_top_2023 = p31_df['nota_iniciativa'].max()
        mean_top_2023 = p31_df['nota_iniciativa'].median() + p31_df['nota_iniciativa'].std()
        mean_bottom_2023 = p31_df['nota_iniciativa'].median() - p31_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p31_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p32':

        outliers_top_2023 = p32_df['nota_iniciativa'].max()
        mean_top_2023 = p32_df['nota_iniciativa'].median() + p32_df['nota_iniciativa'].std()
        mean_bottom_2023 = p32_df['nota_iniciativa'].median() - p32_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p32_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p33':

        outliers_top_2023 = p33_df['nota_iniciativa'].max()
        mean_top_2023 = p33_df['nota_iniciativa'].median() + p33_df['nota_iniciativa'].std()
        mean_bottom_2023 = p33_df['nota_iniciativa'].median() - p33_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p33_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p34':

        outliers_top_2023 = p34_df['nota_iniciativa'].max()
        mean_top_2023 = p34_df['nota_iniciativa'].median() + p34_df['nota_iniciativa'].std()
        mean_bottom_2023 = p34_df['nota_iniciativa'].median() - p34_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p34_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p35':

        outliers_top_2023 = p35_df['nota_iniciativa'].max()
        mean_top_2023 = p35_df['nota_iniciativa'].median() + p35_df['nota_iniciativa'].std()
        mean_bottom_2023 = p35_df['nota_iniciativa'].median() - p35_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p35_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p36':

        outliers_top_2023 = p36_df['nota_iniciativa'].max()
        mean_top_2023 = p36_df['nota_iniciativa'].median() + p36_df['nota_iniciativa'].std()
        mean_bottom_2023 = p36_df['nota_iniciativa'].median() - p36_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p36_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p37':

        outliers_top_2023 = p37_df['nota_iniciativa'].max()
        mean_top_2023 = p37_df['nota_iniciativa'].median() + p37_df['nota_iniciativa'].std()
        mean_bottom_2023 = p37_df['nota_iniciativa'].median() - p37_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p37_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p38':

        outliers_top_2023 = p38_df['nota_iniciativa'].max()
        mean_top_2023 = p38_df['nota_iniciativa'].median() + p38_df['nota_iniciativa'].std()
        mean_bottom_2023 = p38_df['nota_iniciativa'].median() - p38_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p38_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p39':

        outliers_top_2023 = p39_df['nota_iniciativa'].max()
        mean_top_2023 = p39_df['nota_iniciativa'].median() + p39_df['nota_iniciativa'].std()
        mean_bottom_2023 = p39_df['nota_iniciativa'].median() - p39_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p39_df['nota_iniciativa'].min()

    outliers_top.append(outliers_top_2021)
    outliers_top.append(outliers_top_2023)

    mean_top.append(mean_top_2021)
    mean_top.append(mean_top_2023)

    mean_bottom.append(mean_bottom_2021)
    mean_bottom.append(mean_bottom_2023)

    outliers_bottom.append(outliers_bottom_2021)
    outliers_bottom.append(outliers_bottom_2023)


    fig = go.Figure(data=[
        go.Candlestick(
            x=x_axis,
            high=outliers_top,
            open=mean_top,
            close=mean_bottom,
            low=outliers_bottom,
            )
        ],
        ).update_layout(margin={"t":0,"b":0,"l":0,"r":0},xaxis_rangeslider_visible=False)

    return fig

#Callback descarga respuestas 2023
@dash.callback(
    Output("download_respuestas_2023", "data"),
    Input("btn_download_respuestas_2023", "n_clicks"),
    prevent_initial_call=True,
)
def descargar_respuestas_2023(n_clicks):
    path =f'./files/respuestas/2023/respuestas_2023.xlsx'

    return dcc.send_file(path)

#Callback descarga resultados 2023
@dash.callback(
    Output("download_resultados_2023", "data"),
    Input("btn_download_resultados_2023", "n_clicks"),
    prevent_initial_call=True,
)
def descargar_resultados_2023(n_clicks):
    path =f'./files/resultados/2023/resultados_2023.xlsx'

    return dcc.send_file(path)

#Callback descarga individuales
@dash.callback(
    Output("download_repeats", "data"),
    Input("btn_download_repeats", "n_clicks"),
    prevent_initial_call=True,
)
def descargar_individuales(n_clicks):
    path =f'./files/separadas/'
    loczip ='./files/exports/bucles.zip'

    zf = zipfile.ZipFile(loczip, "w")
    for dirname, subdirs, files in os.walk(path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    return dcc.send_file(loczip)