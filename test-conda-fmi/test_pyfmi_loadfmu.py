import contextlib
import pathlib

import numpy
import pyfmi
import pytest

script_path = pathlib.Path(__file__).parent

@pytest.mark.xfail(0,
                   reason="just because")
def test_LoadFmu():
  fmu_path = (pathlib.Path("/pythonfmu") / "examples" / 'Resistor.fmu').resolve()
  print(
    script_path,
    fmu_path,
    flush=True)
  assert fmu_path.is_file()

  model = pyfmi.load_fmu(fmu_path)
  inputs = ('positive_pin_v', lambda t: 20 + 5. * numpy.cos(t))
  res = model.simulate(final_time=30, input=inputs, options={'ncp': 300})


# https://jmodelica.org/pyfmi/pyfmi.html#module-fmi
  with open("logfile", "w") as f:
    with contextlib.redirect_stdout(f):
      print("get_description", model.get_description())
      print("get_categories", model.get_categories())
      print("get_model_variables", model.get_model_variables())
      print("get_input_list", model.get_input_list())
      print("get_output_list", model.get_output_list())
      print("get_states_list", model.get_states_list())
      print("###")
      print(res)
      
  assert True
  
  for k, v in model.get_model_variables().items(): 
      print(k, model.get_variable_causality(k))
  
  
  
  
  
  
  
  
