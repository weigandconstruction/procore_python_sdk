# FormTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Form Template | [optional] 
**description** | **str** | The Description of the Form Template | [optional] 
**fillable_pdf** | **str** | Form&#39;s Fillable PDF. To upload a fillable PDF you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;fillable_pdf&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.form_template1 import FormTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of FormTemplate1 from a JSON string
form_template1_instance = FormTemplate1.from_json(json)
# print the JSON string representation of the object
print(FormTemplate1.to_json())

# convert the object into a dict
form_template1_dict = form_template1_instance.to_dict()
# create an instance of FormTemplate1 from a dict
form_template1_from_dict = FormTemplate1.from_dict(form_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


