# Form2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Form | [optional] 
**description** | **str** | The Description of the Form | [optional] 
**private** | **bool** | The Private status of the Form | [optional] [default to False]
**fillable_pdf_prostore_file_id** | **int** | Form&#39;s Fillable PDF | [optional] 
**prostore_file_ids** | **List[int]** | An array of Prostore File IDs. The Prostore Files will replace the current collection of attachments associated with the Form | [optional] 

## Example

```python
from procore_sdk.models.form2 import Form2

# TODO update the JSON string below
json = "{}"
# create an instance of Form2 from a JSON string
form2_instance = Form2.from_json(json)
# print the JSON string representation of the object
print(Form2.to_json())

# convert the object into a dict
form2_dict = form2_instance.to_dict()
# create an instance of Form2 from a dict
form2_from_dict = Form2.from_dict(form2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


