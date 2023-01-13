# import main

if __name__ == "__main__":
  HEAD = """
  <title>"Hello, World !" example</title>
  <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAMFBMVEUEAvyEhsxERuS8urQsKuycnsRkYtzc2qwUFvRUVtysrrx0ctTs6qTMyrSUksQ0NuyciPBdAAABHklEQVR42mNgwAa8zlxjDd2A4POfOXPmzZkFCAH2M8fNzyALzDlzg2ENssCbMwkMOsgCa858YOjBKxBzRoHhD7LAHiBH5swCT9HQ6A9ggZ4zp7YCrV0DdM6pBpAAG5Blc2aBDZA68wCsZPuZU0BDH07xvHOmAGKKvgMP2NA/Zw7ADIYJXGDgLQeBBSCBFu0aoAPYQUadMQAJAE29zwAVWMCWpgB08ZnDQGsbGhpsgCqBQHNfzRkDEIPlzFmo0T5nzoMovjPHoAK8Zw5BnA5yDosDSAVYQOYMKIDZzkoDzagAsjhqzjRAfXTmzAQgi/vMQZA6pjtAvhEk0E+ATWRRm6YBZuScCUCNN5szH1D4TGdOoSrggtiNAH3vBBjwAQCglIrSZkf1MQAAAABJRU5ErkJggg==" />
  """

  BODY = """
  <fieldset>
    <input id="input" maxlength="20" placeholder="Enter a name here" type="text"
          data-xdh-onevent="Submit" value="World"/>
    <div style="display: flex; justify-content: space-around; margin: 5px auto auto auto;">
    <button data-xdh-onevent="Submit">Submit</button>
    <button data-xdh-onevent="Clear">Clear</button>
    </div>
  </fieldset>
  """

  def ac_connect(dom):
    dom.inner("", BODY )
    dom.focus( "input")

  def ac_submit(dom):
    dom.alert("Hello, {}!".format(dom.get_value("input")))
    dom.focus( "input")

  def ac_clear(dom):
    if dom.confirm("Are you sure?"):
      dom.set_value("input", "" )
    dom.focus( "input")

  callbacks = {
    "": ac_connect,
    "Submit": ac_submit,
    "Clear": ac_clear,
  }

  launch(callbacks, None, HEAD)