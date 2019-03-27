import sys
from setuptools import setup

entry_points = {
    'console_scripts': [
        'knossos_to_stats = klab_utils.knossos_to_stats:main',
        'knossos_to_tif = klab_utils.knossos_to_tif:main',
        'knossos_to_swc = klab_utils.knossos_to_swc:main',
        'swc_to_mask = klab_utils.swc_to_mask:main',
        'labels_to_knossos = klab_utils.labels_to_knossos:main',
        'fiji_stitch = klab_utils.fiji_stitch:main',
        'neuroglance_raw = klab_utils.neuroglance_raw:main',
        'neuroglance_precomputed = klab_utils.neuroglance_precomputed:main',
        'neuroglance_public = klab_utils.neuroglance_public:main',
        'raw_to_precomputed = klab_utils.raw_to_precomputed:main',
        'raw_to_precomputed_v2 = klab_utils.raw_to_precomputed_v2:main',
        'raw_to_precomputed_MPI = klab_utils.raw_to_precomputed_MPI:main',
        'generate_mesh = klab_utils.generate_mesh:main',
        'generate_mesh_manifest = klab_utils.generate_mesh_manifest:main',
        'contrast_adjust = klab_utils.contrast_adjust:main',
        'offset_annotation = klab_utils.offset_annotation:main',
        'EM_preprocess = klab_utils.EM_preprocess:main',
        'EM_trackEM2_preprocess = klab_utils.EM_trackEM2_preprocess:main',
        'generate_prealign_txt = klab_utils.generate_prealign_txt:main',
        'rename_trackEM2 = klab_utils.rename_trackEM2:main',
        'mesh_generator = klab_utils.mesh_generator:main',
        'aligntk_preprocess = klab_utils.aligntk_preprocess:main',
        'aligntk_cut_to_eight = klab_utils.aligntk_cut_to_eight:main',
        'aligntk_gen_mask = klab_utils.aligntk_gen_mask:main',
        'aligntk_gen_mask_v2 = klab_utils.aligntk_gen_mask_v2:main',
        'aligntk_merge_masks = klab_utils.aligntk_merge_masks:main',
        'aligntk_cut = klab_utils.aligntk_cut:main',
        'aligntk_contrast_adjust = klab_utils.aligntk_contrast_adjust:main',
        'aligntk_preview = klab_utils.aligntk_preview:main',
        'aligntk_reduce = klab_utils.aligntk_reduce:main',
        'reduce_resolution = klab_utils.reduce_resolution:main',
        'aligntk_min_rect = klab_utils.aligntk_min_rect:main',
        'mpi_montage = klab_utils.mpi_montage:main'
    ]
}
install_requires = [
    'knossos_utils',
    'tqdm',
    #'cloud-volume',
    #'neuroglancer',
    #'igneous'
]
setup(
    name='klab_utils',
    author='Hanyu Li',
    packages=['klab_utils'],
    entry_points=entry_points,
    include_package_data=True,
    version='1.0',
    description='Various Kasthuri Lab scripts.',
    keywords=['converter', 'skeletonization', 'segmentation'],
    install_requires=install_requires,
)
