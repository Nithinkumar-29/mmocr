_base_ = [
    # 'nrtr_resnet31-1by16-1by8_6e_st_mj.py',
    'nrtr_resnet_indic.py'
]

model = dict(backbone=dict(last_stage_pool=False))
