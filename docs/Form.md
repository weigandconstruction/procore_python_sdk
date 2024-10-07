# Form


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Form | 
**description** | **str** | The Description of the Form | 
**form_template_id** | **int** | ID of the Form Template that the Form is made from | 
**private** | **bool** | The Private status of the Form | [optional] [default to False]
**fillable_pdf_prostore_file_id** | **int** | Form&#39;s Fillable PDF | 
**prostore_file_ids** | **List[int]** | An array of Prostore File IDs. The Prostore Files will be associated with the Form as attachments | [optional] 

## Example

```python
from procore_sdk.models.form import Form

# TODO update the JSON string below
json = "{}"
# create an instance of Form from a JSON string
form_instance = Form.from_json(json)
# print the JSON string representation of the object
print(Form.to_json())

# convert the object into a dict
form_dict = form_instance.to_dict()
# create an instance of Form from a dict
form_from_dict = Form.from_dict(form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


