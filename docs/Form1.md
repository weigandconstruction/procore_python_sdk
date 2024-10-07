# Form1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Form | 
**description** | **str** | The Description of the Form | 
**form_template_id** | **int** | ID of the Form Template that the Form is made from | 
**private** | **bool** | The Private status of the Form | [optional] [default to False]
**fillable_pdf** | **bytearray** | Form&#39;s Fillable PDF. To upload a fillable PDF you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;fillable_pdf&#x60; as files. | 
**attachments** | **List[str]** | Form&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.form1 import Form1

# TODO update the JSON string below
json = "{}"
# create an instance of Form1 from a JSON string
form1_instance = Form1.from_json(json)
# print the JSON string representation of the object
print(Form1.to_json())

# convert the object into a dict
form1_dict = form1_instance.to_dict()
# create an instance of Form1 from a dict
form1_from_dict = Form1.from_dict(form1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


